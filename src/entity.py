from __future__ import annotations

from .context import Context, EntityProvider, ProviderReference


class EntityReference(ProviderReference):
    def __init__(self, entity: EntityProvider) -> None:
        super().__init__(Context(entity=entity))

    def to_string(self) -> str:
        return '@s'


class Entity(EntityProvider):
    def __init__(self) -> None:
        super().__init__(Context(entity=self))

    def get_str_args(self) -> tuple[str, ...]:
        return ()
