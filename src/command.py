from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING

from .context import (
    Context,
    ContextProvider,
    EntityProvider,
    PositionProvider,
    ProviderReference,
)
from .context_node import ContextNode
from .entity import EntityReference
from .position import PositionReference

if TYPE_CHECKING:
    from .function import Function

type CommandArg = str | ProviderReference


class Command(ContextNode):
    _args: list[CommandArg]

    def __init__(self, args: list[CommandArg], *additional_contexts: Context) -> None:
        super().__init__(
            Context.combine(
                *(arg.context for arg in args if isinstance(arg, ProviderReference)),
                *additional_contexts,
            )
        )
        self._args = args

    def to_string(self, context: Context) -> str:
        return ' '.join(self._get_str_args(context))

    def _get_str_args(self, context: Context) -> list[str]:
        providers = self.flattened(context)

        if providers is None:
            raise ValueError

        args: list[str] = []

        for provider in providers:
            args.extend(provider.get_str_args())
            context = context.with_provider(provider)

        if len(args) > 0:
            args.insert(0, 'execute')
            args.append('run')

        for arg in self._args:
            if isinstance(arg, str):
                args.append(arg)
            else:
                args.append(arg.to_string())

        return args

    def flattened(
        self, context: Context, start: Sequence[ContextProvider] | None = None
    ) -> Sequence[ContextProvider] | None:
        if start is None:
            start = []

        if context.is_or_extends(self.context):
            return start

        for node in self.walk(exclude=start):
            if context.is_or_extends(node.context):
                result = self.flattened(context.with_provider(node), [*start, node])
                if result is not None:
                    return result

        return None


class Kill(Command):
    def __init__(self, entity: EntityProvider) -> None:
        super().__init__(['kill', EntityReference(entity)])


class Teleport(Command):
    def __init__(self, entity: EntityProvider, position: PositionProvider) -> None:
        super().__init__(
            ['teleport', EntityReference(entity), PositionReference(position)]
        )


class FunctionCommand(Command):
    def __init__(self, context: Context, function: Function) -> None:
        super().__init__(['function', function.name()], context)
