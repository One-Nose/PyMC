from __future__ import annotations

from .context import Context, EntityProvider, ReferenceProvider


class EntityReference(EntityProvider, ReferenceProvider):
    _entity: EntityProvider

    def __init__(self, entity: EntityProvider) -> None:
        super().__init__(Context())

        self._entity = entity

    def to_string(self, context: Context) -> str:
        if self._entity == context.entity:
            return '@s'
        raise ValueError


class Entity(EntityProvider):
    def __init__(self) -> None:
        super().__init__(Context())
