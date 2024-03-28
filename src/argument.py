from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .entity import Entity
    from .position import Position


class Argument(ABC):
    @abstractmethod
    def to_string(self, entity: Entity | None, position: Position | None) -> str: ...
