from __future__ import annotations

from typing import TYPE_CHECKING, Any, Self

from .arg_command import ArgCommand
from .argument import Argument
from .base_block import BaseBlock
from .context import Context
from .exception import IncompatiblePosition
from .execute import ExecutePositioned

if TYPE_CHECKING:
    from .entity import Entity


class Position(Argument):
    @staticmethod
    def abs(x: float, y: float, z: float) -> AbsolutePosition:
        return AbsolutePosition((x, y, z))

    def set_block(self, block: BaseBlock) -> None:
        ArgCommand('setblock', self, block).add()

    def to_string(self, entity: Entity | None, position: Position | None) -> str:
        entity = entity

        return ' '.join(self.coor_to_string(coor, position) for coor in range(3))

    def coor_to_string(self, coor: int, position: Position | None) -> str:
        coor = coor

        if self == position:
            return '~'
        raise IncompatiblePosition(self, position)

    def __matmul__(self, coors: tuple[float, float, float]) -> Position:
        return RelativePosition(self, coors)

    def __call__(
        self, x: float | None = None, y: float | None = None, z: float | None = None
    ) -> Any:
        return ReplacedPosition(self, (x, y, z))

    def __enter__(self) -> Self:
        ExecutePositioned(self).add()
        return self

    def __exit__(self, exc_type: Exception | None, *_) -> bool:
        Context.get().exit()
        return exc_type is None


class AbsolutePosition(Position):
    coors: tuple[float, float, float]

    def __init__(self, coors: tuple[float, float, float]) -> None:
        super().__init__()

        self.coors = coors

    def coor_to_string(self, coor: int, position: Position | None) -> str:
        position = position

        return str(self.coors[coor])


class ReplacedPosition(Position):
    position: Position
    replacements: tuple[float | None, float | None, float | None]

    def __init__(
        self,
        position: Position,
        replacements: tuple[float | None, float | None, float | None],
    ) -> None:
        super().__init__()

        self.position = position
        self.replacements = replacements

    def coor_to_string(self, coor: int, position: Position | None) -> str:
        if self.replacements[coor] is None:
            return self.position.coor_to_string(coor, position)

        return str(self.replacements[coor])

    def args_list(self) -> list[str]:
        args: list[str] = []

        for i, name in ((0, 'x'), (1, 'y'), (2, 'z')):
            if self.replacements[i] is not None:
                args.append(f'{name}={self.replacements[i]}')

        args.append(str(self.position))

        return args

    def __matmul__(self, coors: tuple[float, float, float]) -> ReplacedPosition:
        return ReplacedPosition(
            RelativePosition(self.position, coors), self.replacements
        )


class RelativePosition(Position):
    position: Position
    offset: tuple[float, float, float]

    def __init__(self, position: Position, offset: tuple[float, float, float]) -> None:
        super().__init__()

        self.position = position
        self.offset = offset

    def coor_to_string(self, coor: int, position: Position | None) -> str:
        if self.position == position:
            if self.offset[coor] == 0:
                return '~'
            return '~' + str(self.offset[coor])

        raise IncompatiblePosition(self, position)

    def __matmul__(self, coors: tuple[float, float, float]) -> RelativePosition:
        return RelativePosition(
            self.position,
            (
                coors[0] + self.offset[0],
                coors[1] + self.offset[1],
                coors[2] + self.offset[2],
            ),
        )

    def args_list(self) -> list[str]:
        args: list[str] = []

        for i in self.offset:
            args.append('0' if i == 0 else f'{i:+}')

        args.append(str(self.position))

        return args
