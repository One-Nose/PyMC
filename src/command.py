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
    def get_args(self) -> list[str | Argument]: ...

    def add(self) -> None:
        Context.get().commands.append(self)

    def to_string(self, entity: Entity | None, position: Position | None) -> str:
        args: list[str] = []

        for arg in self.get_args():
            if isinstance(arg, str):
                args.append(arg)
            else:
                args.append(arg.to_string(entity, position))

        return ' '.join(args)
