from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterator
from typing import TYPE_CHECKING

from .context import Context

if TYPE_CHECKING:
    from .argument import Argument
    from .entity import Entity
    from .position import Position


class Command(ABC):
    def add(self) -> None:
        Context.get().commands.append(self)
        self.update_mark_commands()

        # automark arguments that weren't used immediately
        for arg in Context.get().get_arguments():
            if arg.number == 0:
                arg.mark_always = True

    @abstractmethod
    def to_string(self, entity: Entity | None, position: Position | None) -> str: ...

    @abstractmethod
    def get_mark_arguments(self) -> Iterator[Argument]: ...

    def update_mark_commands(self) -> None:
        for argument in self.get_mark_arguments():
            argument.update_mark_command()

    def args_list(self) -> list[str]:
        return []

    def __repr__(self) -> str:
        return type(self).__name__ + '(' + ', '.join(self.args_list()) + ')'


class MarkCommand(Command):
    command: Command | None

    def __init__(self) -> None:
        super().__init__()

        self.command = None

    def to_string(self, entity: Entity | None, position: Position | None) -> str:
        if self.command is None:
            return ''
        return self.command.to_string(entity, position)

    def get_mark_arguments(self) -> Iterator[Argument]:
        if self.command is not None:
            yield from self.command.get_mark_arguments()
