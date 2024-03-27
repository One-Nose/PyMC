from __future__ import annotations

from typing import Self

from .arg_command import ArgCommand
from .context import Context
from .exception import IncompatibleEntity
from .execute import ExecuteCommand


class Entity:
    def kill(self) -> None:
        ArgCommand('kill', self).add()

    def to_string(self, entity: Entity | None = None) -> str:
        if entity == self:
            return '@s'
        raise IncompatibleEntity

    def __enter__(self) -> Self:
        ExecuteCommand(self).add()
        return self

    def __exit__(self, exc_type: Exception | None, *_) -> bool:
        Context.get().exit()
        return exc_type is None
