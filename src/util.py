from __future__ import annotations

import re
from typing import Self

from .exception import InvalidResourcePath, InvalidResourceString


class ResourceLocation(str):
    def __new__(cls, namespace: ResourceString, path: ResourcePath) -> Self:
        return super().__new__(cls, f'{namespace}:{path}')


class ResourcePath(str):
    def __new__(cls, path: str) -> Self:
        if not re.fullmatch(r'[0-9a-z_\-.]+(/[0-9a-z_\-.]+)*', path):
            raise InvalidResourcePath(path)
        return super().__new__(cls, path)


class ResourceString(str):
    def __new__(cls, string: str) -> Self:
        if not re.fullmatch(r'[0-9a-z_\-.]+', string):
            raise InvalidResourceString(string)
        return super().__new__(cls, string)
