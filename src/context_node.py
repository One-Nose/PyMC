from __future__ import annotations

from abc import ABC
from collections.abc import Generator, Iterable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .context import Context, ContextProvider


class ContextNode(ABC):
    context: Context

    def __init__(self, context: Context) -> None:
        self.context = context

    def walk(
        self, exclude: Iterable[ContextProvider] | None = None
    ) -> Generator[ContextProvider, None, None]:
        if exclude is None:
            exclude = []

        new_exclude = [*exclude]

        for arg in self.context.providers():
            if arg not in new_exclude:
                new_exclude.append(arg)
                yield arg
                yield from arg.walk(exclude=new_exclude)
