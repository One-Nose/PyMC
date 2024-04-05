from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Generator
from typing import NamedTuple

from .context_node import ContextNode


class Context(NamedTuple):
    entity: EntityProvider | None = None
    position: PositionProvider | None = None

    @staticmethod
    def combine(*contexts: Context) -> Context:
        result = Context()

        for context in contexts:
            if context.conflicts_with(result):
                raise ValueError
            result = result.updated(context)

        return result

    def providers(self) -> Generator[ContextProvider, None, None]:
        for provider in self:  # pylint: disable=not-an-iterable
            if provider is not None:
                yield provider

    def is_or_extends(self, context: Context) -> bool:
        for provider, condition_provider in zip(self, context):
            if condition_provider is not None and provider != condition_provider:
                return False
        return True

    def conflicts_with(self, context: Context) -> bool:
        for provider, other_provider in zip(self, context):
            if (
                provider is not None
                and other_provider is not None
                and provider != other_provider
            ):
                return True
        return False

    def applies_to_template(self, template: Context) -> bool:
        for provider, template_provider in zip(self, template):
            if provider is None and template_provider is not None:
                return False
        return True

    def with_provider(self, provider: ContextProvider) -> Context:
        return self._replace(  # pylint: disable=no-member
            **{provider.provider_type: provider}
        )

    def updated(self, context: Context) -> Context:
        fields = self._asdict()  # pylint: disable=no-member

        for name, provider in context._asdict().items():
            if provider is not None:
                fields[name] = provider

        return Context(**fields)


class ContextProvider(ContextNode):
    provider_type: str

    @abstractmethod
    def get_str_args(self) -> tuple[str, ...]: ...


class EntityProvider(ContextProvider, ABC):
    provider_type = 'entity'


class PositionProvider(ContextProvider, ABC):
    provider_type = 'position'


class ProviderReference(ContextNode):
    def to_string(self) -> str:
        raise ValueError
