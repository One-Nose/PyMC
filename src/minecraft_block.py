from dataclasses import InitVar, dataclass, field

from .block import Block
from .resource_path import ResourceLocation, ResourcePath, ResourceString


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


@dataclass
class TypedBlock[T: str](MinecraftBlock):
    type_name: str = field(init=False)
    prefix: str | None = field(init=False, default=None)
    block_type: InitVar[T]

    def __post_init__(self, block_type: T) -> None:
        self.id = block_type + '_' + self.type_name

        if self.prefix is not None:
            self.id = self.prefix + '_' + self.id

        super().__post_init__()
