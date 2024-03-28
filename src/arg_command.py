from __future__ import annotations

from typing import TYPE_CHECKING

from .command import Command

if TYPE_CHECKING:
    from .argument import Argument
    from .entity import Entity
    from .position import Position


class ArgCommand(Command):
    arguments: list[str | Argument]

    def __init__(self, *arguments: str | Argument) -> None:
        self.arguments = list(arguments)

    def get_args(
        self, entity: Entity | None, position: Position | None
    ) -> list[str | Argument]:
        entity = entity
        position = position

        return self.arguments
