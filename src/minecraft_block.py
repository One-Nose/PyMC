from dataclasses import InitVar, dataclass, field
from enum import StrEnum, auto
from typing import TYPE_CHECKING

from .block import Block
from .resource_path import ResourceLocation, ResourcePath, ResourceString

if TYPE_CHECKING:
    from .block_classes import AnyWoodType


@dataclass
class MinecraftBlock(Block):
    id: str = field(init=False)

    def __post_init__(self) -> None:
        self.block_id = ResourceLocation(
            ResourceString('minecraft'), ResourcePath(ResourceString(self.id))
        )


@dataclass
class SimpleBlock(MinecraftBlock):
    id: str = field(init=True)


class SlabStairsBlock(SimpleBlock):
    pass


class StemBlock(SimpleBlock):
    pass


class StoneType(SimpleBlock):
    pass


type AnySlabStairsBlock = AnyWoodType | StoneType | SlabStairsBlock


class StandardTree(StrEnum):
    OAK = auto()
    SPRUCE = auto()
    BIRCH = auto()
    JUNGLE = auto()
    ACACIA = auto()
    DARK_OAK = auto()
    CHERRY = auto()


class MangroveType(StrEnum):
    MANGROVE = auto()


class Tree:
    ACACIA = StandardTree.ACACIA
    DARK_OAK = StandardTree.DARK_OAK
    CHERRY = StandardTree.CHERRY
    OAK = StandardTree.OAK
    BIRCH = StandardTree.BIRCH
    JUNGLE = StandardTree.JUNGLE
    MANGROVE = MangroveType.MANGROVE
    SPRUCE = StandardTree.SPRUCE


type TreeType = StandardTree | MangroveType


class Fungus(StrEnum):
    CRIMSON = auto()
    WARPED = auto()


@dataclass
class TypedBlock[T: str | MinecraftBlock | type[MinecraftBlock]](MinecraftBlock):
    type_name: str = field(init=False)
    prefix: str | None = field(init=False, default=None)
    block_type: InitVar[T]

    def __post_init__(self, block_type: T) -> None:
        self.id = (
            (block_type if isinstance(block_type, str) else block_type.id)
            + '_'
            + self.type_name
        )

        if self.prefix is not None:
            self.id = self.prefix + '_' + self.id

        super().__post_init__()
