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

    def __matmul__(self, coors: tuple[float, float, float]) -> RelativePosition:
        return RelativePosition(self, *coors)


class RelativePosition(Position):
    position: Position

    x: float
    y: float
    z: float

    def __init__(self, position: Position, x: float, y: float, z: float) -> None:
        super().__init__()

        self.position = position

        self.x = x
        self.y = y
        self.z = z

    def to_string(self, entity: Entity | None, position: Position | None) -> str:
        if self.position == position:
            return ' '.join(
                '~' if coor == 0 else f'~{coor}' for coor in (self.x, self.y, self.z)
            )

        return super().to_string(entity, position)

    def __matmul__(self, coors: tuple[float, float, float]) -> RelativePosition:
        return RelativePosition(
            self.position, self.x + coors[0], self.y + coors[1], self.z + coors[2]
        )
