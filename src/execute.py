from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from .arg_command import ArgCommand
from .command import Argument, Command
from .context import Context
from .util import ResourcePath

if TYPE_CHECKING:
    from .datapack import DataPack
    from .entity import Entity


class ExecuteCommand(Command):
    context: ExecuteContext

    entity: Entity
    command: Command

    def __init__(self, entity: Entity) -> None:
        self.entity = entity

        self.context = ExecuteContext(Context.get().datapack, self, entity)

    def add(self) -> None:
        super().add()
        self.context.enter()

    def get_args(self, entity: Entity | None) -> list[Argument]:
        arguments: list[Argument] = []

        if self.entity != entity:
            arguments.extend(('execute', 'as', self.entity, 'run'))

        return arguments + self.command.get_args(entity)


class ExecuteContext(Context):
    func_id: ClassVar[int] = 0

    command: ExecuteCommand

    def __init__(
        self, datapack: DataPack, command: ExecuteCommand, entity: Entity | None
    ) -> None:
        super().__init__(datapack, entity)

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
