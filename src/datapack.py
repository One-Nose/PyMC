from .resource_path import ResourceString, ResourceStringLike


class DataPack:
    namespace: ResourceString

    def __init__(self, namespace: ResourceStringLike) -> None:
        self.namespace = ResourceString(namespace)
