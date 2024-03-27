from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from .context import Context

if TYPE_CHECKING:
    from .entity import Entity

type Argument = str | Entity


class Command(ABC):
    @abstractmethod
    def get_args(self, entity: Entity | None) -> list[Argument]: ...

    def add(self) -> None:
        Context.get().commands.append(self)

    def to_string(self, entity: Entity | None) -> str:
        return ' '.join(
            [
                arg if isinstance(arg, str) else arg.to_string(entity)
                for arg in self.get_args(entity)
            ]
        )
