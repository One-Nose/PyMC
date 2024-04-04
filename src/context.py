from __future__ import annotations

from abc import abstractmethod
from collections.abc import Generator
from typing import NamedTuple

from .context_node import ContextNode


class Context(NamedTuple):
    entity: EntityProvider | None = None
    position: PositionProvider | None = None

    def providers(self) -> Generator[ContextProvider, None, None]:
        for provider in self:  # pylint: disable=not-an-iterable
            if provider is not None:
                yield provider

    def compatible_with(self, context: Context) -> bool:
        for provider, condition_provider in zip(self, context):
            if provider not in (None, condition_provider):
                return False
        return True

    def applies_to_template(self, template: Context) -> bool:
        for provider, template_provider in zip(self, template):
            if provider is None and template_provider is not None:
                return False
        return True

    def with_provider(self, provider: ContextProvider) -> Context:
        replace_args: dict[str, ContextProvider] = {}

        if isinstance(provider, EntityProvider):
            replace_args['entity'] = provider
        elif isinstance(provider, PositionProvider):
            replace_args['position'] = provider
        else:
            raise TypeError

        return self._replace(**replace_args)  # pylint: disable=no-member


class ContextProvider(ContextNode):
    @abstractmethod
    def get_str_args(self, context: Context) -> tuple[str, ...]: ...


class ReferenceProvider(ContextProvider):
    @abstractmethod
    def to_string(self, context: Context) -> str: ...


class EntityProvider(ContextProvider):
    def get_str_args(self, context: Context) -> tuple[str, ...]:
        if self == context.entity:
            return ()
        raise ValueError


class PositionProvider(ContextProvider):
    def get_str_args(self, context: Context) -> tuple[str, ...]:
        if self == context.position:
            return ()
        raise ValueError
