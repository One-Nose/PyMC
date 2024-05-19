from __future__ import annotations

from .context import Context, ContextProvider, ProviderReference
from .entity import DirectEntityReference, EntityProvider


class PositionProvider(ContextProvider):
    provider_type = 'position'

    def as_reference(self) -> PositionReference:
        return DirectPositionReference(self)


class PositionReference(ProviderReference):
    def as_provider(self) -> PositionProvider:
        return Positioned(self)


type AnyPosition = PositionReference | PositionProvider


class DirectPositionReference(PositionReference):
    def __init__(self, position: PositionProvider) -> None:
        super().__init__(Context(position=position))

    def to_string(self) -> str:
        return '~ ~ ~'


class RelativePosition(PositionReference):
    _offset: tuple[float, float, float]

    def __init__(
        self, position: AnyPosition, offset: tuple[float, float, float]
    ) -> None:
        super().__init__(Context(position=position.as_provider()))
        self._offset = offset

    def to_string(self) -> str:
        return ' '.join('~' if offset == 0 else f'~{offset}' for offset in self._offset)


class AbsolutePosition(PositionReference):
    _coors: tuple[float, float, float]

    def __init__(self, coors: tuple[float, float, float]) -> None:
        super().__init__(Context())
        self._coors = coors

    def to_string(self) -> str:
        return ' '.join(str(coor) for coor in self._coors)


class Position(PositionProvider):
    def __init__(self) -> None:
        super().__init__(Context(position=self))


class Positioned(PositionProvider):
    position: PositionReference

    def __init__(self, position: AnyPosition) -> None:
        super().__init__(position.context)

        self.position = position.as_reference()

    def get_str_args(self) -> tuple[str, ...]:
        return ('positioned', self.position.to_string())


class PositionedAs(PositionProvider):
    entity: EntityProvider

    def __init__(self, entity: EntityProvider) -> None:
        super().__init__(Context(entity=entity))

        self.entity = entity

    def get_str_args(self) -> tuple[str, ...]:
        return ('positioned', 'as', DirectEntityReference(self.entity).to_string())
