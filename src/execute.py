from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, ClassVar

from .arg_command import ArgCommand
from .argument import Argument
from .command import Command
from .context import Context
from .util import ResourcePath

if TYPE_CHECKING:
    from .entity import Entity
    from .position import Position


class ExecuteCommand(Command, ABC):
    context: ExecuteContext
    command: Command

    def __init__(self, entity: Entity | None, position: Position | None) -> None:
        super().__init__()
        self.context = ExecuteContext(Context.get(), self, entity, position)

    def add(self) -> None:
        super().add()
        self.context.enter()

    @abstractmethod
    def get_mark_arguments(self) -> list[Argument]: ...

    def update_mark_commands(self) -> None:
        for arg in self.get_mark_arguments():
            arg.update_mark_command()

    @abstractmethod
    def get_arguments(self) -> list[str | Argument]: ...

    def get_args(self) -> list[str | Argument]:
        arguments: list[str | Argument] = [
            'execute',
            *self.get_arguments(),
            'run',
        ]

        return arguments

    def get_command_string(
        self, entity: Entity | None, position: Position | None
    ) -> str:
        return self.command.to_string(entity, position)

    def is_redundant(self, entity: Entity | None, position: Position | None) -> bool:
        entity = entity
        position = position

        return False

    def to_string(self, entity: Entity | None, position: Position | None) -> str:
        if self.is_redundant(entity, position):
            return self.command.to_string(entity, position)

        self_string = ArgCommand(*self.get_args()).to_string(entity, position)
        command_string = self.get_command_string(entity, position)

        if command_string.startswith('execute '):
            return self_string[: -len('run')] + command_string[len('execute ') :]

        return self_string + ' ' + command_string

    def __enter__(self) -> ExecuteContext:
        self.add()
        return self.context

    def __exit__(self, exc_type: type[BaseException] | None, *_) -> bool:
        self.context.exit()
        return exc_type is None

    def args_list(self) -> list[str]:
        return [repr(arg) for arg in self.get_arguments()]


class ExecuteAs(ExecuteCommand):
    def __init__(self, entity: Entity) -> None:
        super().__init__(entity, None)

    def get_arguments(self) -> list[str | Argument]:
        assert self.context.entity is not None

        return ['as', self.context.entity]

    def get_mark_arguments(self) -> list[Argument]:
        assert self.context.entity is not None

        return [self.context.entity]

    def is_redundant(self, entity: Entity | None, position: Position | None) -> bool:
        return super().is_redundant(entity, position) or self.context.entity == entity

    def get_command_string(
        self, entity: Entity | None, position: Position | None
    ) -> str:
        entity = entity

        return super().get_command_string(self.context.entity, position)


class ExecutePositioned(ExecuteCommand):
    def __init__(self, position: Position) -> None:
        super().__init__(None, position)

    def get_arguments(self) -> list[str | Argument]:
        assert self.context.position is not None

        return ['positioned', self.context.position]

    def get_mark_arguments(self) -> list[Argument]:
        assert self.context.position is not None

        return [self.context.position]

    def is_redundant(self, entity: Entity | None, position: Position | None) -> bool:
        return (
            super().is_redundant(entity, position) or self.context.position == position
        )

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
        parent: Context,
        command: ExecuteCommand,
        entity: Entity | None,
        position: Position | None,
    ) -> None:
        super().__init__(parent, entity, position)

        self.command = command

    def exit(self) -> None:
        super().exit()

        func_path = ResourcePath(f'execute_context_{ExecuteContext.func_id}')
        ExecuteContext.func_id += 1

        self.datapack.micro_functions[func_path] = self
        self.command.command = ArgCommand(
            'function',
            self.datapack.micro_resource_location(func_path),
        )
