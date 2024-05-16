from __future__ import annotations

import re
from typing import overload

type ResourceLocationLike = ResourceLocation | ResourcePathLike
type ResourcePathLike = ResourcePath | ResourceStringLike
type ResourceStringLike = ResourceString | str


class Repr:
    def __repr__(self) -> str:  # pragma: no cover
        return type(self).__name__ + f'({self})'


class ResourceString(Repr):
    _string: str

    def __init__(self, string: ResourceStringLike) -> None:
        if isinstance(string, ResourceString):
            self._string = string._string
        else:
            assert re.fullmatch(r'[0-9a-z_\-.]+', string)
            self._string = string

    def __str__(self) -> str:
        return self._string


class ResourcePath(Repr):
    _path: tuple[ResourceString, ...]

    def __init__(self, path: ResourcePathLike, /, *rest: ResourceStringLike) -> None:
        parts: list[ResourceString] = []

        if isinstance(path, ResourcePath):
            parts += path._path
        else:
            parts.append(ResourceString(path))

        parts.extend(ResourceString(part) for part in rest)

        self._path = tuple(parts)

    def __str__(self) -> str:
        return '/'.join(str(part) for part in self._path)


class ResourceLocation(Repr):
    namespace: ResourceString
    path: ResourcePath

    @overload
    def __init__(self, location: ResourceLocationLike, /) -> None: ...
    @overload
    def __init__(
        self, namespace: ResourceStringLike, path: ResourcePathLike, /
    ) -> None: ...

    def __init__(
        self,
        namespace_or_location: ResourceLocationLike,
        path: ResourcePathLike | None = None,
        /,
    ):
        if path is None:
            location = namespace_or_location
            if isinstance(location, ResourceLocation):
                self.namespace = location.namespace
                self.path = location.path
            else:
                self.namespace = ResourceString('minecraft')
                self.path = ResourcePath(location)
        else:
            namespace: ResourceStringLike = (
                namespace_or_location  # pyright: ignore[reportAssignmentType]
            )
            self.namespace = ResourceString(namespace)
            self.path = ResourcePath(path)

    def __str__(self) -> str:
        return f'{self.namespace}:{self.path}'
