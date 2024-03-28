from __future__ import annotations

from typing import TYPE_CHECKING

from .arg_command import ArgCommand
from .argument import Argument
from .base_block import BaseBlock
from .exception import IncompatiblePosition

if TYPE_CHECKING:
    from .entity import Entity


class Position(Argument):
    def set_block(self, block: BaseBlock) -> None:
        ArgCommand('setblock', self, block).add()

    def to_string(self, entity: Entity | None, position: Position | None) -> str:
        entity = entity

        if position == self:
            return '~ ~ ~'
        raise IncompatiblePosition
