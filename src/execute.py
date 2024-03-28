from __future__ import annotations

from abc import ABC, abstractmethod
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


class ExecuteCommand(Command, ABC):
    context: ExecuteContext
    command: Command

    def __init__(self, entity: Entity | None, position: Position | None) -> None:
        super().__init__()
        self.context = ExecuteContext(Context.get().datapack, self, entity, position)

    def add(self) -> None:
        super().add()
        self.context.enter()

    @abstractmethod
    def get_arguments(
        self, entity: Entity | None, position: Position | None
    ) -> list[str | Argument]: ...

    def get_args(
        self, entity: Entity | None, position: Position | None
    ) -> list[str | Argument]:
        arguments: list[str | Argument] = [
            'execute',
            *self.get_arguments(entity, position),
            'run',
        ]

        return arguments

    def get_command_string(
        self, entity: Entity | None, position: Position | None
    ) -> str:
        return self.command.to_string(entity, position)

    def to_string(self, entity: Entity | None, position: Position | None) -> str:
        string = super().to_string(entity, position)

        if string == 'execute run':
            return self.command.to_string(entity, position)

        self_string = super().to_string(entity, position)
        command_string = self.get_command_string(entity, position)

        if command_string.startswith('execute '):
            return self_string[: -len('run')] + command_string[len('execute ') :]

        return self_string + ' ' + command_string

    def __enter__(self) -> ExecuteContext:
        self.add()
        return self.context

    def __exit__(self, exc_type: Exception | None, *_) -> bool:
        self.context.exit()
        return exc_type is None


class ExecuteAs(ExecuteCommand):
    def __init__(self, entity: Entity) -> None:
        super().__init__(entity, None)

    def get_arguments(
        self, entity: Entity | None, position: Position | None
    ) -> list[str | Argument]:
        position = position

        assert self.context.entity is not None

        if self.context.entity == entity:
            return []

        return ['as', self.context.entity]

    def get_command_string(
        self, entity: Entity | None, position: Position | None
    ) -> str:
        entity = entity

        return super().get_command_string(self.context.entity, position)


class ExecutePositioned(ExecuteCommand):
    def __init__(self, position: Position) -> None:
        super().__init__(None, position)

    def get_arguments(
        self, entity: Entity | None, position: Position | None
    ) -> list[str | Argument]:
        entity = entity

        assert self.context.position is not None

        if self.context.position == position:
            return []

        return ['positioned', self.context.position]

    def get_command_string(
        self, entity: Entity | None, position: Position | None
    ) -> str:
        position = position

        return super().get_command_string(entity, self.context.position)


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
