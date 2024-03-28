from __future__ import annotations

from typing import Self

from .arg_command import ArgCommand
from .argument import Argument
from .context import Context
from .exception import IncompatibleEntity
from .execute import ExecuteCommand
from .position import Position


class Entity(Argument):
    def kill(self) -> None:
        ArgCommand('kill', self).add()

    def to_string(self, entity: Entity | None, position: Position | None) -> str:
        position = position

        if entity == self:
            return '@s'
        raise IncompatibleEntity

    def __enter__(self) -> Self:
        ExecuteCommand(at_entity=self).add()
        return self

    def __exit__(self, exc_type: Exception | None, *_) -> bool:
        Context.get().exit()
        return exc_type is None
