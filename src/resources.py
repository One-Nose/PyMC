from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import TYPE_CHECKING

from .resource_path import ResourceLocation, ResourcePath, ResourcePathLike

if TYPE_CHECKING:
    from .datapack import DataPack


class Resource(ABC):
    _resource_type: str = NotImplemented

    _datapack: DataPack
    _path: ResourcePath

    def __init__(self, datapack: DataPack, path: ResourcePathLike) -> None:
        datapack.register(self)

        self._datapack = datapack
        self._path = ResourcePath(path)

    def inner_path(self) -> Path:
        return Path(self._resource_type, str(self._path))

    def namespaced(self) -> ResourceLocation:
        return ResourceLocation(self._datapack.namespace, self._path)

    @abstractmethod
    def to_string(self) -> str: ...
