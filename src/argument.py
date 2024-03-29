from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from .command import MarkCommand
from .context import Context
from .exception import UnsupportedAutoMark

if TYPE_CHECKING:
    from .entity import Entity
    from .position import Position


class Argument(ABC):
    mark_command: MarkCommand | None

    def __init__(self, automark: bool) -> None:
        super().__init__()

        if automark:
            self.mark_command = MarkCommand()
            self.mark_command.add()
            Context.get().add_argument(self)
        else:
            self.mark_command = None

    def update_mark_command(self) -> None:
        for arg in Context.get().get_arguments():
            if arg.argument == self:
                arg.number += 1

    def mark(self) -> None:
        raise UnsupportedAutoMark

    @abstractmethod
    def to_string(self, entity: Entity | None, position: Position | None) -> str: ...

    def args_list(self) -> list[str]:
        return [hex(id(self))]

    def __repr__(self) -> str:
        return type(self).__name__ + '(' + ', '.join(self.args_list()) + ')'
