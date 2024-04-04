from __future__ import annotations

from abc import ABC
from collections.abc import Generator, Sequence
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .context import Context, ContextProvider


class ContextNode(ABC):
    _context: Context

    def __init__(self, context: Context) -> None:
        self._context = context

    def walk(
        self, exclude: Sequence[ContextProvider] = []
    ) -> Generator[ContextProvider, None, None]:
        new_exclude = [*exclude]

        for arg in self._context.providers():
            if arg not in new_exclude:
                yield arg
                new_exclude.append(arg)
            yield from arg.walk(exclude=new_exclude)

    def flattened(
        self, context: Context, start: Sequence[ContextProvider] = []
    ) -> Sequence[ContextProvider] | None:
        for node in self.walk(exclude=start):
            if node._context.compatible_with(context):
                result = self.flattened(context.with_provider(node), [*start, node])
                if result is not None:
                    return result
        else:
            return start
