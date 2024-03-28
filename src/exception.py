from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.entity import Entity
    from src.position import Position


class MinecraftException(Exception):
    pass


class BadFunctionSignature(MinecraftException):
    pass


class IncompatibleEntity(MinecraftException):
    def __init__(self, entity: Entity, context_entity: Entity | None) -> None:
        super().__init__(
            f'entity {entity} cannot be used with context entity {context_entity}'
        )


class IncompatiblePosition(MinecraftException):
    def __init__(self, position: Position, context_position: Position | None) -> None:
        super().__init__(
            f'position {position} cannot be used'
            f' with context position {context_position}'
        )


class InvalidResourcePath(MinecraftException):
    def __init__(self, path: str) -> None:
        super().__init__(f'resource path {path!r} is invalid')


class InvalidResourceString(MinecraftException):
    def __init__(self, string: str) -> None:
        super().__init__(f'resource string {str!r} is invalid')
