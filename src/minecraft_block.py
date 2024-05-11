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
    type_name: str | None = field(
        init=False, default=None, metadata={'is_state': False}
    )
    prefix: str | None = field(init=False, default=None, metadata={'is_state': False})
    block_type: InitVar[T] = field(metadata={'is_state': False})

    def __post_init__(self, block_type: T) -> None:
        parts: list[str] = []

        if self.prefix is not None:
            parts.append(self.prefix)

        if block_type is not None:
            parts.append(block_type)

        if self.type_name is not None:
            parts.append(self.type_name)

        self.id = '_'.join(parts)

        super().__post_init__()


@dataclass
class OptionalTypedBlock[T: str](TypedBlock[T | None]):
    block_type: InitVar[T | None] = field(default=None, metadata={'is_state': False})

    def __post_init__(self, block_type: T | None) -> None:
        super().__post_init__(block_type)


@dataclass
class ConnectedBlock:
    east: bool | None = None
    north: bool | None = None
    south: bool | None = None
    west: bool | None = None


@dataclass
class Waterloggable:
    waterlogged: bool | None = None
