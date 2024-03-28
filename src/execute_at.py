from __future__ import annotations

from typing import TYPE_CHECKING

from .argument import Argument
from .execute import ExecuteCommand
from .position import Position

if TYPE_CHECKING:
    from .entity import Entity


class ExecuteAt(ExecuteCommand):
    entity: Entity

    def __init__(self, entity: Entity) -> None:
        super().__init__(None, Position())

        self.entity = entity

    def get_arguments(
        self, entity: Entity | None, position: Position | None
    ) -> list[str | Argument]:
        entity = entity
        position = position

        return ['at', self.entity]

    def get_command_string(
        self, entity: Entity | None, position: Position | None
    ) -> str:
        position = position

        return super().get_command_string(entity, self.context.position)
