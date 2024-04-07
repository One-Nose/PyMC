from __future__ import annotations

import re


class ResourceString:
    _string: str

    def __init__(self, string: str) -> None:
        assert re.fullmatch(r'[0-9a-z_\-.]+', string)
        self._string = string

    def __str__(self) -> str:
        return self._string


class ResourcePath:
    _path: tuple[ResourceString, ...]

    def __init__(self, *path: ResourceString) -> None:
        assert len(path) >= 1
        self._path = path

    def __str__(self) -> str:
        return '/'.join(str(part) for part in self._path)


class ResourceLocation:
    namespace: ResourceString
    path: ResourcePath

    def __init__(self, namespace: ResourceString, path: ResourcePath) -> None:
        self.namespace = namespace
        self.path = path

    def __repr__(self) -> str:  # pragma: no cover
        return type(self).__name__ + f'({self})'

    def __str__(self) -> str:
        return f'{self.namespace}:{self.path}'
