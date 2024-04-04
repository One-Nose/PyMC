from __future__ import annotations

from typing import TYPE_CHECKING

from .context import Context, EntityProvider, PositionProvider, ReferenceProvider
from .context_node import ContextNode
from .entity import EntityReference
from .position import PositionReference

if TYPE_CHECKING:
    from .function import Function

type CommandArg = str | ReferenceProvider


class Command(ContextNode):
    _args: list[CommandArg]

    def __init__(self, context: Context, args: list[CommandArg]) -> None:
        super().__init__(context)
        self._args = args

    def to_string(self, context: Context) -> str:
        return ' '.join(self._get_str_args(context))

    def _get_str_args(self, context: Context) -> list[str]:
        providers = self.flattened(context)

        if providers is None:
            raise ValueError

        args: list[str] = []

        for provider in providers:
            args.extend(provider.get_str_args(context))
            context = context.with_provider(provider)

        if len(args) > 0:
            args.insert(0, 'execute')
            args.append('run')

        for arg in self._args:
            if isinstance(arg, str):
                args.append(arg)
            else:
                args.append(arg.to_string(context))

        return args


class Kill(Command):
    def __init__(self, entity: EntityProvider) -> None:
        super().__init__(Context(entity=entity), ['kill', EntityReference(entity)])


class Teleport(Command):
    def __init__(self, entity: EntityProvider, position: PositionProvider) -> None:
        super().__init__(
            Context(entity=entity, position=position),
            ['teleport', EntityReference(entity), PositionReference(position)],
        )


class FunctionCommand(Command):
    def __init__(self, context: Context, function: Function) -> None:
        super().__init__(context, ['function', function.name()])
