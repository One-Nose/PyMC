from collections import UserString
from enum import StrEnum, auto


class Axis(StrEnum):
    X = auto()
    Y = auto()
    Z = auto()


class BambooLeaves(StrEnum):
    LARGE = auto()
    NONE = auto()
    SMALL = auto()


class CurvedRailShape(StrEnum):
    NORTH_EAST = auto()
    NORTH_WEST = auto()
    SOUTH_EAST = auto()
    SOUTH_WEST = auto()


class DoorHalf(StrEnum):
    LOWER = auto()
    UPPER = auto()


class DoubleSlabType(StrEnum):
    DOUBLE = auto()


class Face(StrEnum):
    CEILING = auto()
    FLOOR = auto()
    WALL = auto()


class Half(StrEnum):
    BOTTOM = auto()
    TOP = auto()


class HorizontalDirection(StrEnum):
    EAST = auto()
    NORTH = auto()
    SOUTH = auto()
    WEST = auto()


class Side(StrEnum):
    LEFT = auto()
    RIGHT = auto()


class StairsShape(StrEnum):
    INNER_LEFT = auto()
    INNER_RIGHT = auto()
    OUTER_LEFT = auto()
    OUTER_RIGHT = auto()
    STRAIGHT = auto()


class StraightRailShape(StrEnum):
    EAST_WEST = auto()
    NORTH_SOUTH = auto()


class VerticalDirection(StrEnum):
    DOWN = auto()
    UP = auto()


class WallHeight(StrEnum):
    LOW = auto()
    NONE = auto()
    HIGH = auto()


class Direction:
    DOWN = VerticalDirection.DOWN
    EAST = HorizontalDirection.EAST
    NORTH = HorizontalDirection.NORTH
    SOUTH = HorizontalDirection.SOUTH
    UP = VerticalDirection.UP
    WEST = HorizontalDirection.WEST


class RailShape:
    EAST_WEST = StraightRailShape.EAST_WEST
    NORTH_EAST = CurvedRailShape.NORTH_EAST
    NORTH_SOUTH = StraightRailShape.NORTH_SOUTH
    NORTH_WEST = CurvedRailShape.NORTH_WEST
    SOUTH_EAST = CurvedRailShape.SOUTH_EAST
    SOUTH_WEST = CurvedRailShape.SOUTH_WEST

    class Ascending(UserString):
        def __init__(self, direction: HorizontalDirection) -> None:
            self.data = f'ascending_{direction}'


type AnyDirection = HorizontalDirection | VerticalDirection
type AnyRailShape = AnyStraightRailShape | CurvedRailShape
type AnyStraightRailShape = StraightRailShape | RailShape.Ascending
type SlabType = Half | DoubleSlabType
