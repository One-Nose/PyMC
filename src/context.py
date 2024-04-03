from __future__ import annotations

from abc import abstractmethod
from collections.abc import Generator
from typing import NamedTuple

from .context_node import ContextNode


class Context(NamedTuple):
    entity: Entity | None = None
    position: Position | None = None

    def providers(self) -> Generator[ContextProvider, None, None]:
        for provider in self:
            if provider is not None:
                yield provider

    def compatible_with(self, context: Context) -> bool:
        for provider, condition_provider in zip(self, context):
            if provider not in (None, condition_provider):
                return False

        return True

    def with_provider(self, provider: ContextProvider) -> Context:
        replace_args: dict[str, ContextProvider] = {}

        if isinstance(provider, Entity):
            replace_args['entity'] = provider
        elif isinstance(provider, Position):
            replace_args['position'] = provider
        else:
            raise TypeError

        return self._replace(**replace_args)


class ContextProvider(ContextNode):
    @abstractmethod
    def get_str_args(self, context: Context) -> tuple[str, ...]: ...

    @abstractmethod
    def to_string(self, context: Context) -> str: ...


class Entity(ContextProvider):
    def get_str_args(self, context: Context) -> tuple[str, ...]:
        if self == context.entity:
            return ()
        raise ValueError

    def to_string(self, context: Context) -> str:
        if self == context.entity:
            return '@s'
        raise ValueError


class Position(ContextProvider):
    def get_str_args(self, context: Context) -> tuple[str, ...]:
        if self == context.position:
            return ()
        raise ValueError

    def to_string(self, context: Context) -> str:
        if self == context.position:
            return '~ ~ ~'
        raise ValueError
