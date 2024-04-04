from __future__ import annotations

from .context import Context, EntityProvider, ProviderReference


class EntityReference(EntityProvider, ProviderReference):
    def get_str_args(self) -> tuple[str, ...]:
        if self == self.context.entity:
            return ()
        return ('as', self.to_string())

    def to_string(self) -> str:
        if self == self.context.entity:
            return '@s'
        return self._as_string()

    def _as_string(self) -> str:
        raise ValueError


class Entity(EntityReference):
    def __init__(self) -> None:
        super().__init__(Context(entity=self))


class DirectEntityReference(EntityReference):
    def __init__(self, entity: EntityProvider) -> None:
        super().__init__(Context(entity=entity))

    def _as_string(self) -> str:
        return '@s'
