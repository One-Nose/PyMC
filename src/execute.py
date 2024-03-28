from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from .arg_command import ArgCommand
from .argument import Argument
from .command import Command
from .context import Context
from .util import ResourcePath

if TYPE_CHECKING:
    from .datapack import DataPack
    from .entity import Entity
    from .position import Position


class ExecuteCommand(Command):
    context: ExecuteContext

    at_entity: Entity | None
    positioned: Position | None

    command: Command

    def __init__(
        self, at_entity: Entity | None = None, positioned: Position | None = None
    ) -> None:
        self.at_entity = at_entity
        self.positioned = positioned

        self.context = ExecuteContext(
            Context.get().datapack, self, at_entity, positioned
        )

    def add(self) -> None:
        super().add()
        self.context.enter()

    def get_args(
        self, entity: Entity | None, position: Position | None
    ) -> list[str | Argument]:
        arguments: list[str | Argument] = ['execute']

        if self.at_entity is not None and self.at_entity != entity:
            arguments.extend(('as', self.at_entity))

        if self.positioned is not None and self.positioned != position:
            arguments.extend(('positioned', self.positioned))

        if len(arguments) > 1:
            arguments.append('run')
        else:
            arguments = []

        if isinstance(self.command, ExecuteCommand):
            return arguments[:-1] + self.command.get_args(entity, position)[1:]

        return arguments + self.command.get_args(entity, position)


class ExecuteContext(Context):
    func_id: ClassVar[int] = 0

    command: ExecuteCommand

    def __init__(
        self,
        datapack: DataPack,
        command: ExecuteCommand,
        entity: Entity | None,
        position: Position | None,
    ) -> None:
        super().__init__(datapack, entity, position)

        self.command = command

    def exit(self) -> None:
        super().exit()

        if len(self.commands) == 1:
            self.command.command = self.commands[0]
        else:
            func_path = ResourcePath(f'execute_context_{ExecuteContext.func_id}')

            self.datapack.micro_functions[func_path] = self
            self.command.command = ArgCommand(
                'function',
                self.datapack.micro_resource_location(func_path),
            )
