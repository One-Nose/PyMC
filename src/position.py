from __future__ import annotations

from .context import Context, EntityProvider, PositionProvider, ReferenceProvider
from .entity import EntityReference
from .exception import IncompatibleContextProvider


class PositionReference(PositionProvider, ReferenceProvider):
    _position: PositionProvider

    def __init__(self, position: PositionProvider) -> None:
        super().__init__(Context())

        self._position = position

    def to_string(self, context: Context) -> str:
        if self._position == context.position:
            return '~ ~ ~'
        raise ValueError


class Position(PositionProvider):
    def __init__(self) -> None:
        super().__init__(Context())


class PositionedAs(PositionProvider):
    entity: EntityProvider

    def __init__(self, entity: EntityProvider) -> None:
        super().__init__(Context(entity=entity))

        self.entity = entity

    def get_str_args(self, context: Context) -> tuple[str, ...]:
        try:
            return super().get_str_args(context)
        except IncompatibleContextProvider:
            return ('positioned', 'as', EntityReference(self.entity).to_string(context))
