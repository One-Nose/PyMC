from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from .context import Context

if TYPE_CHECKING:
    from .argument import Argument
    from .entity import Entity
    from .position import Position


class Command(ABC):
    @abstractmethod
    def get_args(
        self, entity: Entity | None, position: Position | None
    ) -> list[str | Argument]: ...

    def add(self) -> None:
        Context.get().commands.append(self)

    def to_string(self, entity: Entity | None, position: Position | None) -> str:
        return ' '.join(
            [
                arg if isinstance(arg, str) else arg.to_string(entity, position)
                for arg in self.get_args(entity, position)
            ]
        )
