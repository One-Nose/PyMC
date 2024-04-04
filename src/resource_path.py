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

    def namespaced(self, namespace: ResourceString) -> str:
        return f'{namespace}:{self}'

    def __str__(self) -> str:
        return '/'.join(str(part) for part in self._path)
