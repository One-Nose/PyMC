from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .minecraft_block import (
    ConnectedBlock,
    MinecraftBlock,
    OptionalTypedBlock,
    TypedBlock,
    Waterloggable,
)

type Color = Literal['black', 'blue', 'brown', 'cyan']
type CoralType = Literal['brain', 'bubble']
type FungusType = Literal['crimson', 'warped']
type HeadType = Literal['creeper']
type MushroomType = Literal['brown']
type SandType = Literal['red']
type StandardTree = Literal[
    'oak', 'spruce', 'birch', 'jungle', 'acacia', 'dark_oak', 'cherry'
]
type SlabBlock = SlabStairsBlock | Literal['cut_red_sandstone', 'cut_sandstone']
type SlabStairsBlock = WoodType | StoneType | Literal[
    'bamboo_mosaic', 'cut_copper', 'dark_prismarine'
]
type StemBlock = Literal['melon']
type StoneType = Literal[
    'andesite', 'blackstone', 'brick', 'cobbled_deepslate', 'cobblestone'
]
type Tree = StandardTree | Literal['mangrove']
type WoodType = Tree | FungusType | Literal['bamboo']


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
class Air(OptionalTypedBlock[Literal['cave']]):
    type_name = 'air'


class Amethyst:
    class Block(MinecraftBlock):
        id = 'amethyst_block'

    class Budding(MinecraftBlock):
        id = 'budding_amethyst'

    @dataclass
    class Cluster(Waterloggable, MinecraftBlock):
        id = 'amethyst_cluster'

        facing: Direction | None = None


class AncientDebris(MinecraftBlock):
    id = 'ancient_debris'


class Andesite(MinecraftBlock):
    id = 'andesite'


@dataclass
class Anvil(OptionalTypedBlock[Literal['chipped', 'damaged']]):
    id = 'anvil'

    facing: HorizontalDirection | None = None


class Azalea(MinecraftBlock):
    id = 'azalea'


@dataclass
class Bamboo(MinecraftBlock):
    id = 'bamboo'

    age: Literal[0, 1] | None = None
    leaves: Literal['large', 'none', 'small'] | None = None
    stage: Literal[0, 1] | None = None

    class Mosaic(MinecraftBlock):
        id = 'bamboo_mosaic'

    class Shoot(MinecraftBlock):
        id = 'bamboo_sapling'

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


class Beacon(MinecraftBlock):
    id = 'beacon'


@dataclass
class Bed(TypedBlock[Color]):
    type_name = 'bed'

    facing: HorizontalDirection | None = None
    occupied: bool | None = None
    part: Literal['foot', 'head'] | None = None


class Bedrock(MinecraftBlock):
    id = 'bedrock'


@dataclass
class BeeHouse(TypedBlock[Literal['bee_nest', 'beehive']]):
    facing: HorizontalDirection | None = None
    honey_level: Literal[0, 1, 2, 3, 4, 5] | None = None


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


@dataclass
class Blackstone(
    TypedBlock[Literal['chiseled_polished', 'cracked_polished', 'polished']]
):
    type_name = 'blackstone'


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
class Bookshelf(MinecraftBlock):
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


@dataclass
class BrewingStand(MinecraftBlock):
    id = 'brewing_stand'

    has_bottle_0: bool | None = None
    has_bottle_1: bool | None = None
    has_bottle_2: bool | None = None


class Bricks(MinecraftBlock):
    id = 'bricks'


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


class Calcite(MinecraftBlock):
    id = 'calcite'


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


class CartographyTable(MinecraftBlock):
    id = 'cartography_table'


class Cauldron(MinecraftBlock):
    id = 'cauldron'


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


class Clay(MinecraftBlock):
    id = 'clay'


@dataclass
class CommandBlock(OptionalTypedBlock[Literal['chain']]):
    id = 'command_block'

    conditional: bool | None = None
    facing: Direction | None = None


class Coal:
    class Block(MinecraftBlock):
        id = 'coal_block'

    class Ore(MinecraftBlock):
        id = 'coal_ore'


class Cobblestone(MinecraftBlock):
    id = 'cobblestone'


class Cobweb(MinecraftBlock):
    id = 'cobweb'


@dataclass
class Cocoa(MinecraftBlock):
    id = 'cocoa'

    age: Literal[0, 1, 2] | None = None
    facing: HorizontalDirection | None = None


@dataclass
class Composter(MinecraftBlock):
    id = 'composter'

    level: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8] | None = None


@dataclass
class Concrete(TypedBlock[Color]):
    type_name = 'concrete'

    @dataclass
    class Powder(TypedBlock[Color]):
        type_name = 'concrete_powder'


@dataclass
class Conduit(Waterloggable, MinecraftBlock):
    id = 'conduit'


class Copper:
    class Block(MinecraftBlock):
        id = 'copper_block'

    class Cut(MinecraftBlock):
        id = 'cut_copper'

    class Ore(MinecraftBlock):
        id = 'copper_ore'


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


class CraftingTable(MinecraftBlock):
    id = 'crafting_table'


@dataclass
class DaylightDetector(MinecraftBlock):
    id = 'daylight_detector'

    inverted: bool | None = None
    power: Nibble | None = None


@dataclass
class Deepslate(MinecraftBlock):
    id = 'deepslate'

    axis: Axis | None = None

    @dataclass
    class Bricks(OptionalTypedBlock[Literal['cracked']]):
        type_name = 'deepslate_bricks'

    @dataclass
    class Tiles(OptionalTypedBlock[Literal['cracked']]):
        type_name = 'deepslate_tiles'

    @dataclass
    class Variant(TypedBlock[Literal['chiseled', 'cobbled']]):
        type_name = 'deepslate'


@dataclass
class Dirt(OptionalTypedBlock[Literal['coarse']]):
    type_name = 'dirt'


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


@dataclass
class Flower(
    TypedBlock[
        Literal['allium', 'azure_bluet', 'blue_orchid', 'cornflower', 'dandelion']
    ]
):
    pass


@dataclass
class Fungus(TypedBlock[FungusType]):
    type_name = 'fungus'


@dataclass
class Glass(MinecraftBlock):
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


@dataclass
class Head(TypedBlock[HeadType]):
    type_name = 'head'

    powered: bool | None = None
    rotation: Nibble | None = None

    @dataclass
    class Wall(TypedBlock[HeadType]):
        type_name = 'wall_head'

        powered: bool | None = None
        facing: HorizontalDirection | None = None


@dataclass
class Hyphae(TypedBlock[FungusType]):
    type_name = 'hyphae'

    axis: Axis | None = None


@dataclass
class Ice(OptionalTypedBlock[Literal['blue']]):
    type_name = 'ice'


@dataclass
class Leaves(Waterloggable, TypedBlock[Tree | Literal['azalea']]):
    type_name = 'leaves'

    distance: Literal[1, 2, 3, 4, 5, 6, 7] | None = None
    persistent: bool | None = None


@dataclass
class Log(TypedBlock[Tree]):
    type_name = 'log'

    axis: Axis | None = None


class Melon(MinecraftBlock):
    id = 'melon'


@dataclass
class Mushroom(TypedBlock[MushroomType]):
    type_name = 'mushroom'

    @dataclass
    class Block(ConnectedBlock, TypedBlock[MushroomType]):
        type_name = 'mushroom_block'

        down: bool | None = None
        up: bool | None = None


@dataclass
class NetherBricks(OptionalTypedBlock[Literal['chiseled', 'cracked']]):
    type_name = 'nether_bricks'


@dataclass
class Nylium(TypedBlock[FungusType]):
    type_name = 'nylium'


@dataclass
class Obsidian(OptionalTypedBlock[Literal['crying']]):
    type_name = 'obsidian'


@dataclass
class Planks(TypedBlock[WoodType]):
    type_name = 'planks'


@dataclass
class PressurePlate(TypedBlock[WoodType]):
    type_name = 'pressure_plate'

    powered: bool | None = None


@dataclass
class Prismarine(OptionalTypedBlock[Literal['dark']]):
    type_name = 'prismarine'


@dataclass
class Pumpkin(MinecraftBlock):
    id = 'pumpkin'

    @dataclass
    class Carved(MinecraftBlock):
        id = 'carved_pumpkin'

        facing: HorizontalDirection | None = None


@dataclass
class QuartzBlock(OptionalTypedBlock[Literal['chiseled']]):
    type_name = 'quartz_block'


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


class Redstone:
    @dataclass
    class Comparator(MinecraftBlock):
        id = 'comparator'

        facing: HorizontalDirection | None = None
        mode: Literal['compare', 'subtract'] | None = None
        powered: bool | None = None


@dataclass
class Roots(TypedBlock[FungusType]):
    type_name = 'roots'


@dataclass
class Sandstone(OptionalTypedBlock[SandType]):
    type_name = 'sandstone'

    @dataclass
    class Chiseled(OptionalTypedBlock[SandType]):
        type_name = 'sandstone'
        prefix = 'chiseled'

    @dataclass
    class Cut(OptionalTypedBlock[SandType]):
        type_name = 'sandstone'
        prefix = 'cut'


@dataclass
class Sapling(TypedBlock[StandardTree]):
    type_name = 'sapling'

    stage: Literal[0, 1] | None = None


@dataclass
class _SculkSensor(Waterloggable, MinecraftBlock):
    power: Nibble | None = None
    sculk_sensor_phase: Literal['active', 'cooldown', 'inactive'] | None = None


@dataclass
class Sculk(MinecraftBlock):
    id = 'sculk'

    @dataclass
    class Sensor(_SculkSensor):
        id = 'sculk_sensor'

        @dataclass
        class Calibrated(_SculkSensor):
            id = 'calibrated_sculk_sensor'

            facing: HorizontalDirection | None = None


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
class Slab(Waterloggable, TypedBlock[SlabBlock]):
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
    class Fungus(TypedBlock[FungusType]):
        type_name = 'stem'

        axis: Axis | None = None


@dataclass
class Stone(MinecraftBlock):
    id = 'stone'

    @dataclass
    class Bricks(OptionalTypedBlock[Literal['chiseled', 'cracked']]):
        type_name = 'stone_bricks'


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
