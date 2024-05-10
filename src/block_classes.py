from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .minecraft_block import MinecraftBlock, OptionalTypedBlock, SimpleBlock, TypedBlock

type Color = Literal['black', 'blue', 'brown']
type CoralType = Literal['brain', 'bubble']
type Fungus = Literal['crimson', 'warped']
type MushroomType = Literal['brown']
type StandardTree = Literal[
    'oak', 'spruce', 'birch', 'jungle', 'acacia', 'dark_oak', 'cherry'
]
type SlabStairsBlock = WoodType | StoneType | Literal['bamboo_mosaic']
type StemBlock = Literal['melon']
type StoneType = Literal['andesite', 'blackstone', 'brick']
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


AIR = SimpleBlock('air')


class Amethyst:
    BLOCK = SimpleBlock('amethyst_block')
    BUDDING = SimpleBlock('budding_amethyst')

    @dataclass
    class Cluster(MinecraftBlock):
        id = 'amethyst_cluster'

        facing: Direction | None = None
        waterlogged: bool | None = None

        block_states = 'facing', 'waterlogged'


ANCIENT_DEBRIS = SimpleBlock('ancient_debris')
ANDESITE = SimpleBlock('andesite')


@dataclass
class Anvil(MinecraftBlock):
    id = 'anvil'

    facing: HorizontalDirection | None = None

    block_states = ('facing',)


AZALEA = SimpleBlock('azalea')


@dataclass
class Bamboo(MinecraftBlock):
    id = 'bamboo'

    age: Literal[0, 1] | None = None
    leaves: Literal['large', 'none', 'small'] | None = None
    stage: Literal[0, 1] | None = None

    block_states = 'age', 'leaves', 'stage'

    MOSAIC = SimpleBlock('bamboo_mosaic')
    SAPLING = SimpleBlock('bamboo_sapling')

    @dataclass
    class Block(MinecraftBlock):
        id = 'bamboo_block'

        axis: Axis | None = None

        block_states = ('axis',)


@dataclass
class Banner(TypedBlock[Color]):
    type_name = 'banner'

    rotation: Rotation | None = None

    block_states = ('rotation',)

    @dataclass
    class Wall(TypedBlock[Color]):
        type_name = 'wall_banner'

        facing: HorizontalDirection | None = None

        block_states = ('facing',)


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


BEACON = SimpleBlock('beacon')


@dataclass
class Bed(TypedBlock[Color]):
    type_name = 'bed'

    facing: HorizontalDirection | None = None
    occupied: bool | None = None
    part: Literal['foot', 'head'] | None = None

    block_states = 'facing', 'occupied', 'part'


BEDROCK = SimpleBlock('bedrock')


@dataclass
class _BeeHouse(MinecraftBlock):
    facing: HorizontalDirection | None = None
    honey_level: Literal[0, 1, 2, 3, 4, 5] | None = None

    block_states = 'facing', 'honey_level'


@dataclass
class BeeNest(_BeeHouse):
    id = 'bee_nest'


@dataclass
class Beehive(_BeeHouse):
    id = 'beehive'


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
class Blackstone(MinecraftBlock):
    id = 'blackstone'


@dataclass
class BlastFurnace(MinecraftBlock):
    id = 'blast_furnace'

    facing: HorizontalDirection | None = None
    lit: bool | None = None

    block_states = 'facing', 'lit'


@dataclass
class BoneBlock(MinecraftBlock):
    id = 'bone_block'

    axis: Axis | None = None

    block_states = ('axis',)


BOOKSHELF = SimpleBlock('bookshelf')


@dataclass
class BrewingStand(MinecraftBlock):
    id = 'brewing_stand'

    has_bottle_0: bool | None = None
    has_bottle_1: bool | None = None
    has_bottle_2: bool | None = None

    block_states = 'has_bottle_0', 'has_bottle_1', 'has_bottle_2'


BRICKS = SimpleBlock('bricks')


@dataclass
class BubbleColumn(MinecraftBlock):
    id = 'bubble_column'

    drag: bool | None = None

    block_states = ('drag',)


@dataclass
class Button(TypedBlock[WoodType]):
    type_name = 'button'

    face: Literal['ceiling', 'floor', 'wall'] | None = None
    facing: HorizontalDirection | None = None
    powered: bool | None = None

    block_states = 'face', 'facing', 'powered'


@dataclass
class Cake(MinecraftBlock):
    id = 'cake'

    bites: Literal[0, 1, 2, 3, 4, 5, 6] | None = None

    block_states = ('bites',)

    @dataclass
    class Candle(TypedBlock[Color]):
        type_name = 'candle_cake'

        lit: bool | None = None

        block_states = ('lit',)


@dataclass
class Candle(TypedBlock[Color]):
    type_name = 'candle'

    candles: Literal[1, 2, 3, 4] | None = None
    lit: bool | None = None
    waterlogged: bool | None = None

    block_states = 'candles', 'lit', 'waterlogged'


@dataclass
class Carpet(TypedBlock[Color]):
    type_name = 'carpet'


@dataclass
class Concrete(TypedBlock[Color]):
    type_name = 'concrete'

    @dataclass
    class Powder(TypedBlock[Color]):
        type_name = 'concrete_powder'


@dataclass
class Door(TypedBlock[WoodType]):
    type_name = 'door'

    facing: HorizontalDirection | None = None
    half: Literal['lower', 'upper'] | None = None
    hinge: Literal['left', 'right'] | None = None
    open: bool | None = None
    powered: bool | None = None

    block_states = 'facing', 'half', 'hinge', 'open', 'powered'


@dataclass
class Coral(TypedBlock[CoralType]):
    type_name = 'coral'

    waterlogged: bool | None = None

    block_states = ('waterlogged',)

    @dataclass
    class Block(TypedBlock[CoralType]):
        type_name = 'coral_block'

    @dataclass
    class Fan(TypedBlock[CoralType]):
        type_name = 'coral_fan'

        waterlogged: bool | None = None

        block_states = ('waterlogged',)

        @dataclass
        class Wall(TypedBlock[CoralType]):
            type_name = 'coral_wall_fan'

            facing: HorizontalDirection | None = None
            waterlogged: bool | None = None

            block_states = 'facing', 'waterlogged'


class Dripleaf:
    @dataclass
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
    class Gate(TypedBlock[WoodType]):
        type_name = 'fence_gate'

        facing: HorizontalDirection | None = None
        in_wall: bool | None = None
        open: bool | None = None
        powered: bool | None = None

        block_states = 'facing', 'in_wall', 'open', 'powered'


class Flower:
    ALLIUM = SimpleBlock('allium')
    AZURE_BLUET = SimpleBlock('azure_bluet')
    BLUE_ORCHID = SimpleBlock('blue_orchid')


@dataclass
class _GlassPane(MinecraftBlock):
    east: bool | None = None
    north: bool | None = None
    south: bool | None = None
    waterlogged: bool | None = None
    west: bool | None = None

    block_states = 'east', 'north', 'south', 'waterlogged', 'west'


@dataclass
class _Glass(MinecraftBlock):
    id = 'glass'

    @dataclass
    class Pane(_GlassPane):
        id = 'glass_pane'

        @dataclass
        class Stained(_GlassPane, TypedBlock[Color]):
            type_name = 'stained_glass_pane'

    @dataclass
    class Stained(TypedBlock[Color]):
        type_name = 'stained_glass'


GLASS = _Glass()


@dataclass
class Hyphae(TypedBlock[Fungus]):
    type_name = 'hyphae'

    axis: Axis | None = None

    block_states = ('axis',)


@dataclass
class _Ice(MinecraftBlock):
    id = 'ice'

    BLUE = SimpleBlock('blue_ice')


ICE = _Ice()


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


MELON = SimpleBlock('melon')


@dataclass
class Mushroom(TypedBlock[MushroomType]):
    type_name = 'mushroom'

    @dataclass
    class Block(TypedBlock[MushroomType]):
        type_name = 'mushroom_block'

        east: bool | None = None
        down: bool | None = None
        north: bool | None = None
        south: bool | None = None
        up: bool | None = None
        west: bool | None = None

        block_states = 'east', 'down', 'north', 'south', 'up', 'west'


@dataclass
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
class ShulkerBox(OptionalTypedBlock[Color]):
    type_name = 'shulker_box'

    facing: Direction | None = None

    block_states = ('facing',)


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
class Terracotta(OptionalTypedBlock[Color]):
    type_name = 'terracotta'

    @dataclass
    class Glazed(TypedBlock[Color]):
        type_name = 'glazed_terracotta'

        facing: HorizontalDirection | None = None

        block_states = ('facing',)


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


@dataclass
class Wool(TypedBlock[Color]):
    type_name = 'wool'
