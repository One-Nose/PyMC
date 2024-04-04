from __future__ import annotations

from .context import Context, EntityProvider, PositionProvider, ProviderReference
from .entity import EntityReference


class PositionReference(ProviderReference):
    def __init__(self, position: PositionProvider) -> None:
        super().__init__(Context(position=position))

    def to_string(self) -> str:
        return '~ ~ ~'


class Position(PositionProvider):
    def __init__(self) -> None:
        super().__init__(Context(position=self))

    def get_str_args(self) -> tuple[str, ...]:
        return ()


class PositionedAs(PositionProvider):
    entity: EntityProvider

    def __init__(self, entity: EntityProvider) -> None:
        super().__init__(Context(entity=entity))

        self.entity = entity

    def get_str_args(self) -> tuple[str, ...]:
        return ('positioned', 'as', EntityReference(self.entity).to_string())
