from __future__ import annotations

from collections.abc import Generator
from contextlib import contextmanager
from typing import Self

from .arg_command import ArgCommand
from .argument import Argument
from .context import Context
from .exception import IncompatibleEntity
from .execute import ExecuteAs
from .execute_at import ExecuteAt
from .position import Position


class Entity(Argument):
    @staticmethod
    def all() -> AllEntities:
        return AllEntities()

    @contextmanager
    def position(self) -> Generator[Position, None, None]:
        with ExecuteAt(self) as context:
            assert context.position is not None
            yield context.position

    def teleport(self, position: Position) -> None:
        ArgCommand('teleport', self, position).add()

    def kill(self) -> None:
        ArgCommand('kill', self).add()

    def to_string(self, entity: Entity | None, position: Position | None) -> str:
        position = position

        if entity == self:
            return '@s'
        raise IncompatibleEntity(self, entity)

    def __enter__(self) -> Self:
        ExecuteAs(self).add()
        return self

    def __exit__(self, exc_type: Exception | None, *_) -> bool:
        Context.get().exit()
        return exc_type is None


class AllEntities(Entity):
    def to_string(self, entity: Entity | None, position: Position | None) -> str:
        entity = entity
        position = position

        return '@e'
