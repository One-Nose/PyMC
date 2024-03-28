from __future__ import annotations

from typing import TYPE_CHECKING

from .argument import Argument
from .exception import IncompatiblePosition

if TYPE_CHECKING:
    from .entity import Entity


class Position(Argument):
    def to_string(self, entity: Entity | None, position: Position | None) -> str:
        entity = entity

        if position == self:
            return '~ ~ ~'
        raise IncompatiblePosition
