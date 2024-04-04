from __future__ import annotations

from .context import Context, EntityProvider, PositionProvider, ProviderReference
from .entity import DirectEntityReference


class PositionReference(PositionProvider, ProviderReference):
    def get_str_args(self) -> tuple[str, ...]:
        if self == self.context.position:
            return ()
        return ('positioned', self.to_string())

    def to_string(self) -> str:
        if self == self.context.position:
            return '~ ~ ~'
        return self._as_string()

    def _as_string(self) -> str:
        raise ValueError


class DirectPositionReference(PositionReference):
    def __init__(self, position: PositionProvider) -> None:
        super().__init__(Context(position=position))

    def _as_string(self) -> str:
        return '~ ~ ~'


class Position(PositionReference):
    def __init__(self) -> None:
        super().__init__(Context(position=self))


class PositionedAs(PositionProvider):
    entity: EntityProvider

    def __init__(self, entity: EntityProvider) -> None:
        super().__init__(Context(entity=entity))

        self.entity = entity

    def get_str_args(self) -> tuple[str, ...]:
        return ('positioned', 'as', DirectEntityReference(self.entity).to_string())
