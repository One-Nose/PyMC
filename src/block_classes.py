from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .minecraft_block import (
    ConnectedBlock,
    MinecraftBlock,
    OptionalTypedBlock,
    SimpleBlock,
    TypedBlock,
    Waterloggable,
)

type Color = Literal['black', 'blue', 'brown']
type CoralType = Literal['brain', 'bubble']
type Fungus = Literal['crimson', 'warped']
type MushroomType = Literal['brown']
type SandType = Literal['red']
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
type Nibble = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
type StraightRailShape = Literal[
    'ascending_east',
    'ascending_north',
    'ascending_south',
    'ascending_west',
    'east_west',
    'north_south',
]
type WallHeight = Literal['low', 'none', 'high']


@dataclass
class _Air(MinecraftBlock):
    id = 'air'

    CAVE = SimpleBlock('cave_air')


AIR = _Air()


class Amethyst:
    BLOCK = SimpleBlock('amethyst_block')
    BUDDING = SimpleBlock('budding_amethyst')

    @dataclass
    class Cluster(Waterloggable, MinecraftBlock):
        id = 'amethyst_cluster'

        facing: Direction | None = None


ANCIENT_DEBRIS = SimpleBlock('ancient_debris')
ANDESITE = SimpleBlock('andesite')


@dataclass
class Anvil(MinecraftBlock):
    id = 'anvil'

    facing: HorizontalDirection | None = None

    @dataclass
    class Chipped(MinecraftBlock):
        id = 'chipped_anvil'

        facing: HorizontalDirection | None = None


AZALEA = SimpleBlock('azalea')


@dataclass
class Bamboo(MinecraftBlock):
    id = 'bamboo'

    age: Literal[0, 1] | None = None
    leaves: Literal['large', 'none', 'small'] | None = None
    stage: Literal[0, 1] | None = None

    MOSAIC = SimpleBlock('bamboo_mosaic')
    SHOOT = SimpleBlock('bamboo_sapling')

    @dataclass
    class Block(MinecraftBlock):
        id = 'bamboo_block'

        axis: Axis | None = None


@dataclass
class Banner(TypedBlock[Color]):
    type_name = 'banner'

    rotation: Nibble | None = None

    @dataclass
    class Wall(TypedBlock[Color]):
        type_name = 'wall_banner'

        facing: HorizontalDirection | None = None


@dataclass
class Barrel(MinecraftBlock):
    id = 'barrel'

    facing: Direction | None = None
    open: bool | None = None


@dataclass
class Barrier(Waterloggable, MinecraftBlock):
    id = 'barrier'


@dataclass
class Basalt(MinecraftBlock):
    id = 'basalt'

    axis: Axis | None = None


BEACON = SimpleBlock('beacon')


@dataclass
class Bed(TypedBlock[Color]):
    type_name = 'bed'

    facing: HorizontalDirection | None = None
    occupied: bool | None = None
    part: Literal['foot', 'head'] | None = None


BEDROCK = SimpleBlock('bedrock')


@dataclass
class _BeeHouse(MinecraftBlock):
    facing: HorizontalDirection | None = None
    honey_level: Literal[0, 1, 2, 3, 4, 5] | None = None


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


@dataclass
class Bell(MinecraftBlock):
    id = 'bell'

    attachment: Literal['ceiling', 'double_wall', 'floor', 'single_wall'] | None = None
    facing: HorizontalDirection | None = None
    powered: bool | None = None


class _PolisedBlackstone(MinecraftBlock):
    id = 'polished_blackstone'

    CHISELED = SimpleBlock('chiseled_polished_blackstone')


@dataclass
class _Blackstone(MinecraftBlock):
    id = 'blackstone'

    POLISHED = _PolisedBlackstone()


BLACKSTONE = _Blackstone()


@dataclass
class BlastFurnace(MinecraftBlock):
    id = 'blast_furnace'

    facing: HorizontalDirection | None = None
    lit: bool | None = None


@dataclass
class BoneBlock(MinecraftBlock):
    id = 'bone_block'

    axis: Axis | None = None


@dataclass
class _Bookshelf(MinecraftBlock):
    id = 'bookshelf'

    @dataclass
    class Chiseled(MinecraftBlock):
        id = 'chiseled_bookshelf'

        facing: HorizontalDirection | None = None
        slot_0_occupied: bool | None = None
        slot_1_occupied: bool | None = None
        slot_2_occupied: bool | None = None
        slot_3_occupied: bool | None = None
        slot_4_occupied: bool | None = None
        slot_5_occupied: bool | None = None


BOOKSHELF = _Bookshelf()


@dataclass
class BrewingStand(MinecraftBlock):
    id = 'brewing_stand'

    has_bottle_0: bool | None = None
    has_bottle_1: bool | None = None
    has_bottle_2: bool | None = None


BRICKS = SimpleBlock('bricks')


@dataclass
class BubbleColumn(MinecraftBlock):
    id = 'bubble_column'

    drag: bool | None = None


@dataclass
class Button(TypedBlock[WoodType]):
    type_name = 'button'

    face: Literal['ceiling', 'floor', 'wall'] | None = None
    facing: HorizontalDirection | None = None
    powered: bool | None = None


@dataclass
class Cactus(MinecraftBlock):
    id = 'cactus'

    age: Nibble | None = None


@dataclass
class Cake(MinecraftBlock):
    id = 'cake'

    bites: Literal[0, 1, 2, 3, 4, 5, 6] | None = None

    @dataclass
    class Candle(OptionalTypedBlock[Color]):
        type_name = 'candle_cake'

        lit: bool | None = None


CALCITE = SimpleBlock('calcite')


@dataclass
class Campfire(Waterloggable, MinecraftBlock):
    id = 'campfire'

    facing: HorizontalDirection | None = None
    lit: bool | None = None
    signal_fire: bool | None = None


@dataclass
class Candle(Waterloggable, OptionalTypedBlock[Color]):
    type_name = 'candle'

    candles: Literal[1, 2, 3, 4] | None = None
    lit: bool | None = None


@dataclass
class Carpet(TypedBlock[Color]):
    type_name = 'carpet'


@dataclass
class Carrots(MinecraftBlock):
    id = 'carrots'

    age: Literal[0, 1, 2, 3, 4, 5, 6, 7] | None = None


CARTOGRAPHY_TABLE = SimpleBlock('cartography_table')
CAULDRON = SimpleBlock('cauldron')


@dataclass
class Chain(Waterloggable, MinecraftBlock):
    id = 'chain'

    axis: Axis | None = None


@dataclass
class Chest(Waterloggable, MinecraftBlock):
    id = 'chest'

    facing: HorizontalDirection | None = None
    type: Literal['left', 'right', 'single'] | None = None


class Chorus:
    @dataclass
    class Flower(MinecraftBlock):
        id = 'chorus_flower'

        age: Literal[0, 1, 2, 3, 4, 5] | None = None

    @dataclass
    class Plant(MinecraftBlock):
        id = 'chorus_plant'

        down: bool | None = None
        up: bool | None = None


CLAY = SimpleBlock('clay')


@dataclass
class CommandBlock(OptionalTypedBlock[Literal['chain']]):
    id = 'command_block'

    conditional: bool | None = None
    facing: Direction | None = None


@dataclass
class Concrete(TypedBlock[Color]):
    type_name = 'concrete'

    @dataclass
    class Powder(TypedBlock[Color]):
        type_name = 'concrete_powder'


@dataclass
class Coral(Waterloggable, TypedBlock[CoralType]):
    type_name = 'coral'

    @dataclass
    class Block(TypedBlock[CoralType]):
        type_name = 'coral_block'

    @dataclass
    class Fan(Waterloggable, TypedBlock[CoralType]):
        type_name = 'coral_fan'

        @dataclass
        class Wall(Waterloggable, TypedBlock[CoralType]):
            type_name = 'coral_wall_fan'

            facing: HorizontalDirection | None = None


@dataclass
class Deepslate(MinecraftBlock):
    id = 'deepslate'

    axis: Axis | None = None

    CHISELED = SimpleBlock('chiseled_deepslate')


@dataclass
class Door(TypedBlock[WoodType]):
    type_name = 'door'

    facing: HorizontalDirection | None = None
    half: Literal['lower', 'upper'] | None = None
    hinge: Literal['left', 'right'] | None = None
    open: bool | None = None
    powered: bool | None = None


class Dripleaf:
    @dataclass
    class Big(Waterloggable, MinecraftBlock):
        id = 'big_dripleaf'

        facing: HorizontalDirection | None = None
        tilt: Literal['full', 'none', 'partial', 'unstable'] | None = None

        @dataclass
        class Stem(Waterloggable, MinecraftBlock):
            id = 'big_dripleaf_stem'

            facing: HorizontalDirection | None = None


@dataclass
class Fence(Waterloggable, ConnectedBlock, TypedBlock[WoodType]):
    type_name = 'fence'

    @dataclass
    class Gate(TypedBlock[WoodType]):
        type_name = 'fence_gate'

        facing: HorizontalDirection | None = None
        in_wall: bool | None = None
        open: bool | None = None
        powered: bool | None = None


class Flower:
    ALLIUM = SimpleBlock('allium')
    AZURE_BLUET = SimpleBlock('azure_bluet')
    BLUE_ORCHID = SimpleBlock('blue_orchid')


@dataclass
class _Glass(MinecraftBlock):
    id = 'glass'

    @dataclass
    class Pane(Waterloggable, ConnectedBlock, MinecraftBlock):
        id = 'glass_pane'

        @dataclass
        class Stained(Waterloggable, ConnectedBlock, TypedBlock[Color]):
            type_name = 'stained_glass_pane'

    @dataclass
    class Stained(TypedBlock[Color]):
        type_name = 'stained_glass'


GLASS = _Glass()


@dataclass
class Hyphae(TypedBlock[Fungus]):
    type_name = 'hyphae'

    axis: Axis | None = None


@dataclass
class _Ice(MinecraftBlock):
    id = 'ice'

    BLUE = SimpleBlock('blue_ice')


ICE = _Ice()


@dataclass
class Leaves(Waterloggable, TypedBlock[Tree | Literal['azalea']]):
    type_name = 'leaves'

    distance: Literal[1, 2, 3, 4, 5, 6, 7] | None = None
    persistent: bool | None = None


@dataclass
class Log(TypedBlock[Tree]):
    type_name = 'log'

    axis: Axis | None = None


MELON = SimpleBlock('melon')


@dataclass
class Mushroom(TypedBlock[MushroomType]):
    type_name = 'mushroom'

    @dataclass
    class Block(ConnectedBlock, TypedBlock[MushroomType]):
        type_name = 'mushroom_block'

        down: bool | None = None
        up: bool | None = None


@dataclass
class _NetherBricks(MinecraftBlock):
    id = 'nether_bricks'

    CHISELED = SimpleBlock('chiseled_nether_bricks')


NETHER_BRICKS = _NetherBricks()


@dataclass
class Planks(TypedBlock[WoodType]):
    type_name = 'planks'


@dataclass
class PressurePlate(TypedBlock[WoodType]):
    type_name = 'pressure_plate'

    powered: bool | None = None


@dataclass
class _Pumpkin(MinecraftBlock):
    id = 'pumpkin'

    @dataclass
    class Carved(MinecraftBlock):
        id = 'carved_pumpkin'

        facing: HorizontalDirection | None = None


PUMPKIN = _Pumpkin()


@dataclass
class _QuartzBlock(MinecraftBlock):
    id = 'quartz_block'

    CHISELED = SimpleBlock('chiseled_quartz_block')


QUARTZ_BLOCK = _QuartzBlock()


@dataclass
class Rail(Waterloggable, MinecraftBlock):
    id = 'rail'

    shape: (
        StraightRailShape
        | Literal['north_east', 'north_west', 'south_east', 'south_west']
        | None
    ) = None

    @dataclass
    class Activator(Waterloggable, MinecraftBlock):
        id = 'activator_rail'

        powered: bool | None = None
        shape: StraightRailShape | None = None


@dataclass
class Sandstone(OptionalTypedBlock[SandType]):
    type_name = 'sandstone'

    class Chiseled(OptionalTypedBlock[SandType]):
        type_name = 'sandstone'
        prefix = 'chiseled'


@dataclass
class Sapling(TypedBlock[StandardTree]):
    type_name = 'sapling'

    stage: Literal[0, 1] | None = None


@dataclass
class _SculkSensor(Waterloggable, MinecraftBlock):
    power: Nibble | None = None
    sculk_sensor_phase: Literal['active', 'cooldown', 'inactive'] | None = None


@dataclass
class _Sculk(MinecraftBlock):
    id = 'sculk'

    @dataclass
    class Sensor(_SculkSensor):
        id = 'sculk_sensor'

        @dataclass
        class Calibrated(_SculkSensor):
            id = 'calibrated_sculk_sensor'

            facing: HorizontalDirection | None = None


SKULK = _Sculk()


@dataclass
class ShulkerBox(OptionalTypedBlock[Color]):
    type_name = 'shulker_box'

    facing: Direction | None = None


@dataclass
class Sign(Waterloggable, TypedBlock[WoodType]):
    type_name = 'sign'

    rotation: Nibble | None = None

    @dataclass
    class Hanging(Waterloggable, TypedBlock[WoodType]):
        type_name = 'hanging_sign'

        attached: bool | None = None
        rotation: Nibble | None = None

        @dataclass
        class Wall(Waterloggable, TypedBlock[WoodType]):
            type_name = 'wall_hanging_sign'

            facing: HorizontalDirection | None = None

    @dataclass
    class Wall(Waterloggable, TypedBlock[WoodType]):
        type_name = 'wall_sign'

        facing: HorizontalDirection | None = None


@dataclass
class Slab(Waterloggable, TypedBlock[SlabStairsBlock]):
    type_name = 'slab'

    type: Half | Literal['double'] | None = None


@dataclass
class Stairs(Waterloggable, TypedBlock[SlabStairsBlock]):
    type_name = 'stairs'

    facing: HorizontalDirection | None = None
    half: Half | None = None
    shape: (
        Literal['inner_left', 'inner_right', 'outer_left', 'outer_right', 'straight']
        | None
    ) = None


class Stem:
    @dataclass
    class Crop(TypedBlock[StemBlock]):
        type_name = 'stem'

        age: Literal[0, 1, 2, 3, 4, 5, 6, 7] | None = None

        @dataclass
        class Attached(TypedBlock[StemBlock]):
            type_name = 'stem'
            prefix = 'attached'

            facing: HorizontalDirection | None = None

    @dataclass
    class Fungus(TypedBlock[Fungus]):
        type_name = 'stem'

        axis: Axis | None = None


@dataclass
class _StoneBricks(MinecraftBlock):
    id = 'stone_bricks'

    CHISELED = SimpleBlock('chiseled_stone_bricks')


@dataclass
class _Stone(MinecraftBlock):
    id = 'stone'

    STONE_BRICKS = _StoneBricks()


STONE = _Stone()


@dataclass
class Terracotta(OptionalTypedBlock[Color]):
    type_name = 'terracotta'

    @dataclass
    class Glazed(TypedBlock[Color]):
        type_name = 'glazed_terracotta'

        facing: HorizontalDirection | None = None


@dataclass
class Trapdoor(Waterloggable, TypedBlock[WoodType]):
    type_name = 'trapdoor'

    facing: HorizontalDirection | None = None
    half: Half | None = None
    open: bool | None = None
    powered: bool | None = None


@dataclass
class Vines(ConnectedBlock, MinecraftBlock):
    id = 'vine'

    up: bool | None = None

    @dataclass
    class Cave(MinecraftBlock):
        id = 'cave_vines'

        berries: bool | None = None
        age: Nibble | Literal[16, 17, 18, 19, 20, 21, 22, 23, 24, 25] | None = None

        @dataclass
        class Plant(MinecraftBlock):
            id = 'cave_vines_plant'

            berries: bool | None = None


@dataclass
class Wall(Waterloggable, TypedBlock[StoneType]):
    type_name = 'wall'

    east: WallHeight | None = None
    north: WallHeight | None = None
    south: WallHeight | None = None
    up: bool | None = None
    west: WallHeight | None = None


@dataclass
class Wood(TypedBlock[Tree]):
    type_name = 'wood'

    axis: Axis | None = None


@dataclass
class Wool(TypedBlock[Color]):
    type_name = 'wool'
