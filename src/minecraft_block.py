from dataclasses import InitVar, dataclass, field

from .block import Block
from .resource_path import ResourceLocation, ResourcePath, ResourceString


@dataclass
class MinecraftBlock(Block):
    id: str | None = field(init=False, metadata={'is_state': False})

    def __post_init__(self) -> None:
        assert self.id is not None
        self.block_id = ResourceLocation(
            ResourceString('minecraft'), ResourcePath(ResourceString(self.id))
        )


@dataclass
class VariantBlock[T: str | None](MinecraftBlock):
    id: str | None = field(init=False, default=None, metadata={'is_state': False})
    prefix: str | None = field(init=False, default=None, metadata={'is_state': False})
    variant: InitVar[T] = field(metadata={'is_state': False})

    def __post_init__(self, variant: T) -> None:
        parts: list[str] = []

        if self.prefix is not None:
            parts.append(self.prefix)

        if variant is not None:
            parts.append(variant)

        if self.id is not None:
            parts.append(self.id)

        self.id = '_'.join(parts)

        super().__post_init__()


@dataclass
class OptionalVariantBlock[T: str](VariantBlock[T | None]):
    variant: InitVar[T | None] = field(default=None, metadata={'is_state': False})

    def __post_init__(self, variant: T | None) -> None:
        super().__post_init__(variant)


@dataclass
class ConnectedBlock:
    east: bool | None = None
    north: bool | None = None
    south: bool | None = None
    west: bool | None = None


@dataclass
class Waterloggable:
    waterlogged: bool | None = None
