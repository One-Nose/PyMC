import json
from pathlib import Path
from shutil import rmtree
from typing import Any

from .resource_path import ResourceString, ResourceStringLike
from .resources import Resource


class DataPack:
    namespace: ResourceString
    description: str | None
    resources: list[Resource]

    def __init__(
        self, namespace: ResourceStringLike, description: str | None = None
    ) -> None:
        self.namespace = ResourceString(namespace)
        self.description = description
        self.resources = []

    def create(self, output_path: Path) -> None:
        if output_path.exists():
            rmtree(output_path)

        output_path.mkdir()
        self.create_mcmeta(output_path)
        namespace_dir = output_path / 'data' / str(self.namespace)

        for resource in self.resources:
            resource_path = namespace_dir / resource.inner_path()
            resource_path.parent.mkdir(parents=True, exist_ok=True)

            with open(resource_path, 'x') as file:
                file.write(resource.to_string())

    def create_mcmeta(self, output_path: Path) -> None:
        content: dict[str, Any] = {'pack': {'pack_format': 57}}

        if self.description is not None:
            content['pack']['description'] = self.description

        with (output_path / 'pack.mcmeta').open('x') as file:
            json.dump(content, file, indent=2)

    def register(self, resource: Resource) -> None:
        self.resources.append(resource)
