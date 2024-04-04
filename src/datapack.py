from .resource_path import ResourceString


class DataPack:
    namespace: ResourceString

    def __init__(self, namespace: str) -> None:
        self.namespace = ResourceString(namespace)
