from dataclasses import InitVar, dataclass, field

from .block import Block
from .resource_path import ResourceLocation, ResourcePath, ResourceString


@dataclass
class MinecraftBlock(Block):
    id: str = field(init=False, metadata={'is_state': False})

    def __post_init__(self) -> None:
        self.block_id = ResourceLocation(
            ResourceString('minecraft'), ResourcePath(ResourceString(self.id))
        )


@dataclass
class SimpleBlock(MinecraftBlock):
    id: str = field(init=True, metadata={'is_state': False})


@dataclass
class TypedBlock[T: str | None](MinecraftBlock):
    type_name: str = field(init=False, metadata={'is_state': False})
    prefix: str | None = field(init=False, default=None, metadata={'is_state': False})
    block_type: InitVar[T] = field(metadata={'is_state': False})

    def __post_init__(self, block_type: T) -> None:
        self.id = ('' if block_type is None else block_type + '_') + self.type_name

        if self.prefix is not None:
            self.id = self.prefix + '_' + self.id

        super().__post_init__()


@dataclass
class OptionalTypedBlock[T: str](TypedBlock[T | None]):
    block_type: InitVar[T | None] = field(default=None, metadata={'is_state': False})

    def __post_init__(self, block_type: T | None) -> None:
        super().__post_init__(block_type)
