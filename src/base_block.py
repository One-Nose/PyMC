from enum import Enum

from .util import ResourceLocation, ResourcePath, ResourceString


class BaseBlock(ResourceLocation, Enum):
    @staticmethod
    def _generate_next_value_(name: str, *_) -> ResourcePath:
        return ResourcePath(name.lower())


def new_block[T: BaseBlock](cls: type[T], name: ResourcePath, namespace: str) -> T:
    namespace = ResourceString(namespace)
    member: T = ResourceLocation.__new__(cls, namespace, name)
    member._value_ = ResourceLocation(namespace, name)
    return member
