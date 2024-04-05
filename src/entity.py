from __future__ import annotations

from .context import Context, ContextProvider, ProviderReference


class EntityProvider(ContextProvider):
    provider_type = 'entity'

    def as_reference(self) -> EntityReference:
        return DirectEntityReference(self)


class EntityReference(ProviderReference):
    def as_provider(self) -> AsEntity:
        return AsEntity(self)


type AnyEntity = EntityReference | EntityProvider


class DirectEntityReference(EntityReference):
    def __init__(self, entity: EntityProvider) -> None:
        super().__init__(Context(entity=entity))

    def to_string(self) -> str:
        return '@s'


class Entity(EntityProvider):
    def __init__(self) -> None:
        super().__init__(Context(entity=self))


class AsEntity(EntityProvider):
    entity: EntityReference

    def __init__(self, entity: AnyEntity) -> None:
        super().__init__(entity.context)

        self.entity = entity.as_reference()

    def get_str_args(self) -> tuple[str, ...]:
        return ('as', self.entity.to_string())
