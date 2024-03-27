from __future__ import annotations

from typing import TYPE_CHECKING

from .command import Argument, Command

if TYPE_CHECKING:
    from .entity import Entity


class ArgCommand(Command):
    arguments: list[Argument]

    def __init__(self, *arguments: Argument) -> None:
        self.arguments = list(arguments)

    def get_args(self, entity: Entity | None) -> list[Argument]:
        entity = entity
        return self.arguments
