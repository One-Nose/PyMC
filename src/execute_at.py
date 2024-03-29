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

    def get_arguments(self) -> list[str | Argument]:
        return ['at', self.entity]

    def get_command_string(
        self, entity: Entity | None, position: Position | None
    ) -> str:
        position = position

        return super().get_command_string(entity, self.context.position)

    def get_mark_arguments(self) -> list[Argument]:
        assert self.context.position is not None

        return [self.entity, self.context.position]
