from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .minecraft_block import MinecraftBlock, SimpleBlock, TypedBlock

type Fungus = Literal['crimson', 'warped']
type StandardTree = Literal[
    'oak', 'spruce', 'birch', 'jungle', 'acacia', 'dark_oak', 'cherry'
]
type SlabStairsBlock = WoodType | StoneType | Literal['bamboo_mosaic']
type StemBlock = Literal['melon']
type StoneType = Literal['andesite']
type Tree = StandardTree | Literal['mangrove']
type WoodType = Tree | Fungus | Literal['bamboo']


type Axis = Literal['x', 'y', 'z']
type Direction = HorizontalDirection | Literal['down', 'up']
type Half = Literal['bottom', 'top']
type HorizontalDirection = Literal['east', 'north', 'south', 'west']
type Rotation = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
type StraightRailShape = Literal[
    'ascending_east',
    'ascending_north',
    'ascending_south',
    'ascending_west',
    'east_west',
    'north_south',
]
type WallHeight = Literal['low', 'none', 'high']


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


@dataclass
class Bamboo(MinecraftBlock):
    id = 'bamboo'

    age: Literal[0, 1] | None = None
    leaves: Literal['large', 'none', 'small'] | None = None
    stage: Literal[0, 1] | None = None

    block_states = 'age', 'leaves', 'stage'

    MOSAIC = SimpleBlock('bamboo_mosaic')

    @dataclass
    class Block(MinecraftBlock):
        id = 'bamboo_block'

        axis: Axis | None = None

        block_states = ('axis',)


@dataclass
class Barrel(MinecraftBlock):
    id = 'barrel'

    facing: Direction | None = None
    open: bool | None = None

    block_states = 'facing', 'open'


@dataclass
class Barrier(MinecraftBlock):
    id = 'barrier'

    waterlogged: bool | None = None

    block_states = ('waterlogged',)


@dataclass
class Basalt(MinecraftBlock):
    id = 'basalt'

    axis: Axis | None = None

    block_states = ('axis',)


@dataclass
class BeeNest(MinecraftBlock):
    id = 'bee_nest'

    facing: HorizontalDirection | None = None
    honey_level: Literal[0, 1, 2, 3, 4, 5] | None = None

    block_states = 'facing', 'honey_level'


@dataclass
class Beehive(MinecraftBlock):
    id = 'beehive'

    facing: HorizontalDirection | None = None
    honey_level: Literal[0, 1, 2, 3, 4, 5] | None = None

    block_states = 'facing', 'honey_level'


@dataclass
class Beetroots(MinecraftBlock):
    id = 'beetroots'

    age: Literal[0, 1, 2, 3] | None = None

    block_states = ('age',)


@dataclass
class Bell(MinecraftBlock):
    id = 'bell'

    attachment: Literal['ceiling', 'double_wall', 'floor', 'single_wall'] | None = None
    facing: HorizontalDirection | None = None
    powered: bool | None = None

    block_states = 'attachment', 'facing', 'powered'


@dataclass
class Button(TypedBlock[WoodType]):
    type_name = 'button'

    face: Literal['ceiling', 'floor', 'wall'] | None = None
    facing: HorizontalDirection | None = None
    powered: bool | None = None

    block_states = 'face', 'facing', 'powered'


@dataclass
class Door(TypedBlock[WoodType]):
    type_name = 'door'

    facing: HorizontalDirection | None = None
    half: Literal['lower', 'upper'] | None = None
    hinge: Literal['left', 'right'] | None = None
    open: bool | None = None
    powered: bool | None = None

    block_states = 'facing', 'half', 'hinge', 'open', 'powered'


class Dripleaf:
    class Big(MinecraftBlock):
        id = 'big_dripleaf'

        facing: HorizontalDirection | None = None
        tilt: Literal['full', 'none', 'partial', 'unstable'] | None = None
        waterlogged: bool | None = None

        block_states = 'facing', 'tilt', 'waterlogged'

        @dataclass
        class Stem(MinecraftBlock):
            id = 'big_dripleaf_stem'

            facing: HorizontalDirection | None = None
            waterlogged: bool | None = None

            block_states = 'facing', 'waterlogged'


@dataclass
class Fence(TypedBlock[WoodType]):
    type_name = 'fence'

    east: bool | None = None
    north: bool | None = None
    south: bool | None = None
    waterlogged: bool | None = None
    west: bool | None = None

    block_states = 'east', 'north', 'south', 'waterlogged', 'west'


@dataclass
class FenceGate(TypedBlock[WoodType]):
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
class Leaves(TypedBlock[Tree | Literal['azalea']]):
    type_name = 'leaves'

    distance: Literal[1, 2, 3, 4, 5, 6, 7] | None = None
    persistent: bool | None = None
    waterlogged: bool | None = None

    block_states = 'distance', 'persistent', 'waterlogged'


@dataclass
class Log(TypedBlock[Tree]):
    type_name = 'log'

    axis: Axis | None = None

    block_states = ('axis',)


class Planks(TypedBlock[WoodType]):
    type_name = 'planks'


@dataclass
class PressurePlate(TypedBlock[WoodType]):
    type_name = 'pressure_plate'

    powered: bool | None = None

    block_states = ('powered',)


@dataclass
class Rail(MinecraftBlock):
    id = 'rail'

    shape: (
        StraightRailShape
        | Literal['north_east', 'north_west', 'south_east', 'south_west']
        | None
    ) = None
    waterlogged: bool | None = None

    block_states = 'shape', 'waterlogged'

    @dataclass
    class Activator(MinecraftBlock):
        id = 'activator_rail'

        powered: bool | None = None
        shape: StraightRailShape | None = None
        waterlogged: bool | None = None

        block_states = 'powered', 'shape', 'waterlogged'


@dataclass
class Sapling(TypedBlock[StandardTree]):
    type_name = 'sapling'

    stage: Literal[0, 1] | None = None

    block_states = ('stage',)


@dataclass
class Sign(TypedBlock[WoodType]):
    type_name = 'sign'

    rotation: Rotation | None = None
    waterlogged: bool | None = None

    block_states = 'rotation', 'waterlogged'

    @dataclass
    class Hanging(TypedBlock[WoodType]):
        type_name = 'hanging_sign'

        attached: bool | None = None
        rotation: Rotation | None = None
        waterlogged: bool | None = None

        block_states = 'attached', 'rotation', 'waterlogged'

        @dataclass
        class Wall(TypedBlock[WoodType]):
            type_name = 'wall_hanging_sign'

            facing: HorizontalDirection | None = None
            waterlogged: bool | None = None

            block_states = 'facing', 'waterlogged'

    @dataclass
    class Wall(TypedBlock[WoodType]):
        type_name = 'wall_sign'

        facing: HorizontalDirection | None = None
        waterlogged: bool | None = None

        block_states = 'facing', 'waterlogged'


@dataclass
class Slab(TypedBlock[SlabStairsBlock]):
    type_name = 'slab'

    type: Half | Literal['double'] | None = None
    waterlogged: bool | None = None

    block_states = 'type', 'waterlogged'


@dataclass
class Stairs(TypedBlock[SlabStairsBlock]):
    type_name = 'stairs'

    facing: HorizontalDirection | None = None
    half: Half | None = None
    shape: (
        Literal['inner_left', 'inner_right', 'outer_left', 'outer_right', 'straight']
        | None
    ) = None
    waterlogged: bool | None = None

    block_states = 'facing', 'half', 'shape', 'waterlogged'


class Stem:
    @dataclass
    class Crop(TypedBlock[StemBlock]):
        type_name = 'stem'

        age: Literal[0, 1, 2, 3, 4, 5, 6, 7] | None = None

        block_states = ('age',)

        @dataclass
        class Attached(TypedBlock[StemBlock]):
            type_name = 'stem'
            prefix = 'attached'

            facing: HorizontalDirection | None = None

            block_states = ('facing',)

    @dataclass
    class Fungus(TypedBlock[Fungus]):
        type_name = 'stem'

        axis: Axis | None = None

        block_states = ('axis',)


@dataclass
class Trapdoor(TypedBlock[WoodType]):
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
class Wood(TypedBlock[Tree]):
    type_name = 'wood'

    axis: Axis | None = None

    block_states = ('axis',)


class BasicBlock:
    AIR = Air()
    ANCIENT_DEBRIS = SimpleBlock('ancient_debris')
    ANDESITE = SimpleBlock('andesite')
    AZALEA = SimpleBlock('azalea')
    BEACON = SimpleBlock('beacon')
    BEDROCK = SimpleBlock('bedrock')
    MELON = SimpleBlock('melon')
