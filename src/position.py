from __future__ import annotations

from .context import Context, PositionProvider, ReferenceProvider


class PositionReference(PositionProvider, ReferenceProvider):
    position: PositionProvider

    def __init__(self, position: PositionProvider) -> None:
        super().__init__(Context())

        self.position = position

    def to_string(self, context: Context) -> str:
        if self.position == context.position:
            return '~ ~ ~'
        raise ValueError


class Position(PositionProvider):
    def __init__(self) -> None:
        super().__init__(Context())
