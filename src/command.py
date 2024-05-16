from __future__ import annotations

from collections.abc import Sequence
from itertools import chain
from typing import TYPE_CHECKING

from .block_class import Block
from .context import Context, ContextProvider, ProviderReference
from .context_node import ContextNode
from .entity import AnyEntity
from .exception import FlatteningError
from .position import AnyPosition

if TYPE_CHECKING:
    from .function import Function

type CommandArg = str | ProviderReference


class Command(ContextNode):
    _args: list[CommandArg]

    def __init__(
        self,
        args: Sequence[CommandArg | ContextProvider],
        *additional_contexts: Context,
    ) -> None:
        self._args = [
            arg.as_reference() if isinstance(arg, ContextProvider) else arg
            for arg in args
        ]

        super().__init__(
            Context.combine(
                *(
                    arg.context
                    for arg in self._args
                    if isinstance(arg, ProviderReference)
                ),
                *additional_contexts,
            )
        )

    def to_string(self, context: Context) -> str:
        return ' '.join(self._get_str_args(context))

    def _get_str_args(self, context: Context) -> list[str]:
        providers = self.flattened(context)

        if providers is None:
            raise FlatteningError

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

        for node in self.walk(exclude=chain(context.providers(), start)):
            if context.is_or_extends(node.context):
                result = self.flattened(context.with_provider(node), [*start, node])
                if result is not None:
                    return result

        return None


class Kill(Command):
    def __init__(self, entity: AnyEntity) -> None:
        super().__init__(['kill', entity])


class SetBlock(Command):
    def __init__(self, position: AnyPosition, block: Block) -> None:
        super().__init__(['setblock', position, block.to_string()])


class Teleport(Command):
    def __init__(self, entity: AnyEntity, position: AnyPosition) -> None:
        super().__init__(['teleport', entity, position])


class FunctionCommand(Command):
    def __init__(self, context: Context, function: Function) -> None:
        super().__init__(['function', str(function.namespaced())], context)
