import re


class ResourcePath:
    _path: tuple[str, ...]

    def __init__(self, *path: str) -> None:
        self._path = path

        for path_part in self._path:
            assert re.fullmatch(r'[0-9a-z_\-.]+', path_part) is not None
