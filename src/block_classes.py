from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .block_state import (
    AnyRailShape,
    AnyStraightRailShape,
    Axis,
    BambooLeaves,
    Direction,
    DoorHalf,
    Face,
    Half,
    HorizontalDirection,
    Side,
    SlabType,
    StairsShape,
    WallHeight,
)
from .minecraft_block import (
    AnySlabStairsBlock,
    Fungus,
    MinecraftBlock,
    SimpleBlock,
    SlabStairsBlock,
    StandardTree,
    StemBlock,
    StoneType,
    TreeType,
    TypedBlock,
)

type AnyWoodType = TreeType | Fungus | type[Bamboo]


class Air(MinecraftBlock):
    id = 'air'


class Amethyst:
    BLOCK = SimpleBlock('amethyst_block')

    @dataclass
    class Cluster(MinecraftBlock):
        id = 'amethyst_cluster'

        facing: Direction | None = None
        waterlogged: bool | None = None

        block_states = 'facing', 'waterlogged'


@dataclass
class Anvil(MinecraftBlock):
    id = 'anvil'

    facing: HorizontalDirection | None = None

    block_states = ('facing',)


class Azalea(MinecraftBlock):
    id = 'azalea'


@dataclass
class Bamboo(MinecraftBlock):
    id = 'bamboo'

    age: int | None = None
    leaves: BambooLeaves | None = None
    stage: int | None = None

    block_states = 'age', 'leaves', 'stage'

    def __post_init__(self) -> None:
        super().__post_init__()

        assert self.age is None or 0 <= self.age <= 1
        assert self.stage is None or 0 <= self.stage <= 1

    MOSAIC = SlabStairsBlock('bamboo_mosaic')

    @dataclass
    class Block(MinecraftBlock):
        id = 'bamboo_block'

        axis: Axis | None = None

        block_states = ('axis',)


@dataclass
class Button(TypedBlock[AnyWoodType]):
    type_name = 'button'

    face: Face | None = None
    facing: HorizontalDirection | None = None
    powered: bool | None = None

    block_states = 'face', 'facing', 'powered'


@dataclass
class Door(TypedBlock[AnyWoodType]):
    type_name = 'door'

    facing: HorizontalDirection | None = None
    half: DoorHalf | None = None
    hinge: Side | None = None
    open: bool | None = None
    powered: bool | None = None

    block_states = 'facing', 'half', 'hinge', 'open', 'powered'


@dataclass
class Fence(TypedBlock[AnyWoodType]):
    type_name = 'fence'

    east: bool | None = None
    north: bool | None = None
    south: bool | None = None
    waterlogged: bool | None = None
    west: bool | None = None

    block_states = 'east', 'north', 'south', 'waterlogged', 'west'


@dataclass
class FenceGate(TypedBlock[AnyWoodType]):
    type_name = 'fence_gate'

    facing: HorizontalDirection | None = None
    in_wall: bool | None = None
    open: bool | None = None
    powered: bool | None = None

    block_states = 'facing', 'in_wall', 'open', 'powered'


class Flower:
    ALLIUM = SimpleBlock('allium')
    AZURE_BLUET = SimpleBlock('azure_bluet')


@dataclass
class Hyphae(TypedBlock[Fungus]):
    type_name = 'hyphae'

    axis: Axis | None = None

    block_states = ('axis',)


@dataclass
class Leaves(TypedBlock[TreeType | Azalea]):
    type_name = 'leaves'

    distance: int | None = None
    persistent: bool | None = None
    waterlogged: bool | None = None

    block_states = 'distance', 'persistent', 'waterlogged'

    def __post_init__(self, block_type: Any) -> None:
        super().__post_init__(block_type)

        assert self.distance is None or 1 <= self.distance <= 7


@dataclass
class Log(TypedBlock[TreeType]):
    type_name = 'log'

    axis: Axis | None = None

    block_states = ('axis',)


class Planks(TypedBlock[AnyWoodType]):
    type_name = 'planks'


@dataclass
class PressurePlate(TypedBlock[AnyWoodType]):
    type_name = 'pressure_plate'

    powered: bool | None = None

    block_states = ('powered',)


@dataclass
class Rail(MinecraftBlock):
    id = 'rail'

    shape: AnyRailShape | None = None
    waterlogged: bool | None = None

    block_states = 'shape', 'waterlogged'

    @dataclass
    class Activator(MinecraftBlock):
        id = 'activator_rail'

        powered: bool | None = None
        shape: AnyStraightRailShape | None = None
        waterlogged: bool | None = None

        block_states = 'powered', 'shape', 'waterlogged'


@dataclass
class Sapling(TypedBlock[StandardTree]):
    type_name = 'sapling'

    stage: int | None = None

    block_states = ('stage',)

    def __post_init__(self, block_type: Any) -> None:
        super().__post_init__(block_type)

        assert self.stage is None or 0 <= self.stage <= 1


@dataclass
class Sign(TypedBlock[AnyWoodType]):
    type_name = 'sign'

    rotation: int | None = None
    waterlogged: bool | None = None

    block_states = 'rotation', 'waterlogged'

    def __post_init__(self, block_type: Any) -> None:
        super().__post_init__(block_type)

        assert self.rotation is None or 0 <= self.rotation <= 15

    @dataclass
    class Hanging(TypedBlock[AnyWoodType]):
        type_name = 'hanging_sign'

        attached: bool | None = None
        rotation: int | None = None
        waterlogged: bool | None = None

        block_states = 'attached', 'rotation', 'waterlogged'

        def __post_init__(self, block_type: Any) -> None:
            super().__post_init__(block_type)

            assert self.rotation is None or 0 <= self.rotation <= 15

        @dataclass
        class Wall(TypedBlock[AnyWoodType]):
            type_name = 'wall_hanging_sign'

            facing: HorizontalDirection | None = None
            waterlogged: bool | None = None

            block_states = 'facing', 'waterlogged'

    @dataclass
    class Wall(TypedBlock[AnyWoodType]):
        type_name = 'wall_sign'

        facing: HorizontalDirection | None = None
        waterlogged: bool | None = None

        block_states = 'facing', 'waterlogged'


@dataclass
class Slab(TypedBlock[AnySlabStairsBlock]):
    type_name = 'slab'

    type: SlabType | None = None
    waterlogged: bool | None = None

    block_states = 'type', 'waterlogged'


@dataclass
class Stairs(TypedBlock[AnySlabStairsBlock]):
    type_name = 'stairs'

    facing: HorizontalDirection | None = None
    half: Half | None = None
    shape: StairsShape | None = None
    waterlogged: bool | None = None

    block_states = 'facing', 'half', 'shape', 'waterlogged'


class Stem:
    @dataclass
    class Fungus(TypedBlock[Fungus]):
        type_name = 'stem'

        axis: Axis | None = None

        block_states = ('axis',)

    @dataclass
    class Crop(TypedBlock[StemBlock]):
        type_name = 'stem'

        age: int | None = None

        block_states = ('age',)

        def __post_init__(self, block_type: Any) -> None:
            super().__post_init__(block_type)

            assert self.age is None or 0 <= self.age <= 7

        @dataclass
        class Attached(TypedBlock[StemBlock]):
            type_name = 'stem'
            prefix = 'attached'

            facing: HorizontalDirection | None = None

            block_states = ('facing',)


@dataclass
class Trapdoor(TypedBlock[AnyWoodType]):
    type_name = 'trapdoor'

    facing: HorizontalDirection | None = None
    half: Half | None = None
    open: bool | None = None
    powered: bool | None = None
    waterlogged: bool | None = None

    block_states = 'facing', 'half', 'open', 'powered', 'waterlogged'


@dataclass
class Wall(TypedBlock[StoneType]):
    type_name = 'wall'

    east: WallHeight | None = None
    north: WallHeight | None = None
    south: WallHeight | None = None
    up: bool | None = None
    waterlogged: bool | None = None
    west: WallHeight | None = None

    block_states = 'east', 'north', 'south', 'up', 'waterlogged', 'west'


@dataclass
class Wood(TypedBlock[TreeType]):
    type_name = 'wood'

    axis: Axis | None = None

    block_states = ('axis',)


class BasicBlock:
    AIR = Air()
    ANCIENT_DEBRIS = SimpleBlock('ancient_debris')
    ANDESITE = StoneType('andesite')
    AZALEA = Azalea()
    MELON = StemBlock('melon')
