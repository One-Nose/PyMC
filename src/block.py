from enum import Enum, auto
from typing import Self

from .util import ResourceLocation, ResourcePath, ResourceString


class Block(ResourceLocation, Enum):
    @staticmethod
    def _generate_next_value_(name: str, *_) -> ResourcePath:
        return ResourcePath(name.lower())


def new_block[T: Block](cls: type[T], name: ResourcePath, namespace: str) -> T:
    namespace = ResourceString(namespace)
    member: T = ResourceLocation.__new__(cls, namespace, name)
    member._value_ = ResourceLocation(namespace, name)
    return member


class MinecraftBlock(Block):
    def __new__(cls, name: ResourcePath) -> Self:
        return new_block(cls, name, 'minecraft')

    DIAMOND_BLOCK = auto()
