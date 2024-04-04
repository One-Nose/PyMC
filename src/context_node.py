from __future__ import annotations

from abc import ABC
from collections.abc import Generator, Sequence
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .context import Context, ContextProvider


class ContextNode(ABC):
    context: Context

    def __init__(self, context: Context) -> None:
        self.context = context

    def walk(
        self, exclude: Sequence[ContextProvider] | None = None
    ) -> Generator[ContextProvider, None, None]:
        if exclude is None:
            exclude = []

        new_exclude = [*exclude]

        for arg in self.context.providers():
            if arg not in new_exclude:
                yield arg
                new_exclude.append(arg)
            yield from arg.walk(exclude=new_exclude)

    def flattened(
        self, context: Context, start: Sequence[ContextProvider] | None = None
    ) -> Sequence[ContextProvider] | None:
        if start is None:
            start = []

        found_node = False
        for node in self.walk(exclude=start):
            found_node = True

            if node.context.compatible_with(context):
                result = self.flattened(context.with_provider(node), [*start, node])
                if result is not None:
                    return result

        if not found_node:
            return start

        return None
