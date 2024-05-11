from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .minecraft_block import (
    ConnectedBlock,
    MinecraftBlock,
    OptionalVariantBlock,
    VariantBlock,
    Waterloggable,
)

type Color = Literal['black', 'blue', 'brown', 'cyan']
type CoralType = Literal[
    'brain',
    'dead_brain',
    'bubble',
    'dead_bubble',
    'fire',
    'dead_fire',
    'horn',
    'dead_horn',
    'tube',
    'dead_tube',
]
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
    'andesite',
    'blackstone',
    'brick',
    'cobbled_deepslate',
    'cobblestone',
    'deepslate_brick',
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
class Air(OptionalVariantBlock[Literal['cave']]):
    id = 'air'


class Amethyst:
    @dataclass
    class Block(MinecraftBlock):
        id = 'amethyst_block'

    @dataclass
    class Budding(MinecraftBlock):
        id = 'budding_amethyst'

    @dataclass
    class Cluster(Waterloggable, MinecraftBlock):
        id = 'amethyst_cluster'

        facing: Direction | None = None


@dataclass
class AncientDebris(MinecraftBlock):
    id = 'ancient_debris'


@dataclass
class Andesite(MinecraftBlock):
    id = 'andesite'


@dataclass
class Anvil(OptionalVariantBlock[Literal['chipped', 'damaged']]):
    id = 'anvil'

    facing: HorizontalDirection | None = None


@dataclass
class Azalea(MinecraftBlock):
    id = 'azalea'


@dataclass
class Bamboo(MinecraftBlock):
    id = 'bamboo'

    age: Literal[0, 1] | None = None
    leaves: Literal['large', 'none', 'small'] | None = None
    stage: Literal[0, 1] | None = None

    @dataclass
    class Mosaic(MinecraftBlock):
        id = 'bamboo_mosaic'

    @dataclass
    class Shoot(MinecraftBlock):
        id = 'bamboo_sapling'

    @dataclass
    class Block(MinecraftBlock):
        id = 'bamboo_block'

        axis: Axis | None = None


@dataclass
class Banner(VariantBlock[Color]):
    id = 'banner'

    rotation: Nibble | None = None

    @dataclass
    class Wall(VariantBlock[Color]):
        id = 'wall_banner'

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


@dataclass
class Beacon(MinecraftBlock):
    id = 'beacon'


@dataclass
class Bed(VariantBlock[Color]):
    id = 'bed'

    facing: HorizontalDirection | None = None
    occupied: bool | None = None
    part: Literal['foot', 'head'] | None = None


@dataclass
class Bedrock(MinecraftBlock):
    id = 'bedrock'


@dataclass
class BeeHouse(VariantBlock[Literal['bee_nest', 'beehive']]):
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
    VariantBlock[Literal['chiseled_polished', 'cracked_polished', 'polished']]
):
    id = 'blackstone'


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


@dataclass
class Bricks(MinecraftBlock):
    id = 'bricks'


@dataclass
class BubbleColumn(MinecraftBlock):
    id = 'bubble_column'

    drag: bool | None = None


@dataclass
class Button(VariantBlock[WoodType]):
    id = 'button'

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
    class Candle(OptionalVariantBlock[Color]):
        id = 'candle_cake'

        lit: bool | None = None


@dataclass
class Calcite(MinecraftBlock):
    id = 'calcite'


@dataclass
class Campfire(Waterloggable, MinecraftBlock):
    id = 'campfire'

    facing: HorizontalDirection | None = None
    lit: bool | None = None
    signal_fire: bool | None = None


@dataclass
class Candle(Waterloggable, OptionalVariantBlock[Color]):
    id = 'candle'

    candles: Literal[1, 2, 3, 4] | None = None
    lit: bool | None = None


@dataclass
class Carpet(VariantBlock[Color]):
    id = 'carpet'


@dataclass
class Carrots(MinecraftBlock):
    id = 'carrots'

    age: Literal[0, 1, 2, 3, 4, 5, 6, 7] | None = None


@dataclass
class CartographyTable(MinecraftBlock):
    id = 'cartography_table'


@dataclass
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


@dataclass
class Clay(MinecraftBlock):
    id = 'clay'


@dataclass
class CommandBlock(OptionalVariantBlock[Literal['chain']]):
    id = 'command_block'

    conditional: bool | None = None
    facing: Direction | None = None


class Coal:
    @dataclass
    class Block(MinecraftBlock):
        id = 'coal_block'

    @dataclass
    class Ore(OptionalVariantBlock[Literal['deepslate']]):
        id = 'coal_ore'


@dataclass
class Cobblestone(MinecraftBlock):
    id = 'cobblestone'


@dataclass
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
class Concrete(VariantBlock[Color]):
    id = 'concrete'

    @dataclass
    class Powder(VariantBlock[Color]):
        id = 'concrete_powder'


@dataclass
class Conduit(Waterloggable, MinecraftBlock):
    id = 'conduit'


class Copper:
    @dataclass
    class Block(MinecraftBlock):
        id = 'copper_block'

    @dataclass
    class Cut(MinecraftBlock):
        id = 'cut_copper'

    @dataclass
    class Ore(OptionalVariantBlock[Literal['deepslate']]):
        id = 'copper_ore'


@dataclass
class Coral(Waterloggable, VariantBlock[CoralType]):
    id = 'coral'

    @dataclass
    class Block(VariantBlock[CoralType]):
        id = 'coral_block'

    @dataclass
    class Fan(Waterloggable, VariantBlock[CoralType]):
        id = 'coral_fan'

        @dataclass
        class Wall(Waterloggable, VariantBlock[CoralType]):
            id = 'coral_wall_fan'

            facing: HorizontalDirection | None = None


@dataclass
class CraftingTable(MinecraftBlock):
    id = 'crafting_table'


@dataclass
class DaylightDetector(MinecraftBlock):
    id = 'daylight_detector'

    inverted: bool | None = None
    power: Nibble | None = None


@dataclass
class DeadBush(MinecraftBlock):
    id = 'dead_bush'


@dataclass
class DecoratedPot(Waterloggable, MinecraftBlock):
    id = 'decorated_pot'

    facing: HorizontalDirection | None = None
    cracked: bool | None = None


@dataclass
class Deepslate(MinecraftBlock):
    id = 'deepslate'

    axis: Axis | None = None

    @dataclass
    class Bricks(OptionalVariantBlock[Literal['cracked']]):
        id = 'deepslate_bricks'

    @dataclass
    class Tiles(OptionalVariantBlock[Literal['cracked']]):
        id = 'deepslate_tiles'

    @dataclass
    class Variant(VariantBlock[Literal['chiseled', 'cobbled']]):
        id = 'deepslate'


class Diamond:
    @dataclass
    class Ore(OptionalVariantBlock[Literal['deepslate']]):
        id = 'diamond_ore'


@dataclass
class Dirt(OptionalVariantBlock[Literal['coarse']]):
    id = 'dirt'


@dataclass
class Door(VariantBlock[WoodType]):
    id = 'door'

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
class Fence(Waterloggable, ConnectedBlock, VariantBlock[WoodType]):
    id = 'fence'

    @dataclass
    class Gate(VariantBlock[WoodType]):
        id = 'fence_gate'

        facing: HorizontalDirection | None = None
        in_wall: bool | None = None
        open: bool | None = None
        powered: bool | None = None


@dataclass
class Flower(
    VariantBlock[
        Literal['allium', 'azure_bluet', 'blue_orchid', 'cornflower', 'dandelion']
    ]
):
    pass


@dataclass
class Fungus(VariantBlock[FungusType]):
    id = 'fungus'


@dataclass
class Glass(MinecraftBlock):
    id = 'glass'

    @dataclass
    class Pane(Waterloggable, ConnectedBlock, MinecraftBlock):
        id = 'glass_pane'

        @dataclass
        class Stained(Waterloggable, ConnectedBlock, VariantBlock[Color]):
            id = 'stained_glass_pane'

    @dataclass
    class Stained(VariantBlock[Color]):
        id = 'stained_glass'


@dataclass
class Head(VariantBlock[HeadType]):
    id = 'head'

    powered: bool | None = None
    rotation: Nibble | None = None

    @dataclass
    class Wall(VariantBlock[HeadType]):
        id = 'wall_head'

        powered: bool | None = None
        facing: HorizontalDirection | None = None


@dataclass
class Hyphae(VariantBlock[FungusType]):
    id = 'hyphae'

    axis: Axis | None = None


@dataclass
class Ice(OptionalVariantBlock[Literal['blue']]):
    id = 'ice'


@dataclass
class Leaves(Waterloggable, VariantBlock[Tree | Literal['azalea']]):
    id = 'leaves'

    distance: Literal[1, 2, 3, 4, 5, 6, 7] | None = None
    persistent: bool | None = None


@dataclass
class Log(VariantBlock[Tree]):
    id = 'log'

    axis: Axis | None = None


@dataclass
class Melon(MinecraftBlock):
    id = 'melon'


@dataclass
class Mushroom(VariantBlock[MushroomType]):
    id = 'mushroom'

    @dataclass
    class Block(ConnectedBlock, VariantBlock[MushroomType]):
        id = 'mushroom_block'

        down: bool | None = None
        up: bool | None = None


@dataclass
class NetherBricks(OptionalVariantBlock[Literal['chiseled', 'cracked']]):
    id = 'nether_bricks'


@dataclass
class Nylium(VariantBlock[FungusType]):
    id = 'nylium'


@dataclass
class Obsidian(OptionalVariantBlock[Literal['crying']]):
    id = 'obsidian'


@dataclass
class Planks(VariantBlock[WoodType]):
    id = 'planks'


@dataclass
class PressurePlate(VariantBlock[WoodType]):
    id = 'pressure_plate'

    powered: bool | None = None


@dataclass
class Prismarine(OptionalVariantBlock[Literal['dark']]):
    id = 'prismarine'


@dataclass
class Pumpkin(MinecraftBlock):
    id = 'pumpkin'

    @dataclass
    class Carved(MinecraftBlock):
        id = 'carved_pumpkin'

        facing: HorizontalDirection | None = None


@dataclass
class QuartzBlock(OptionalVariantBlock[Literal['chiseled']]):
    id = 'quartz_block'


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
class Roots(VariantBlock[FungusType]):
    id = 'roots'


@dataclass
class Sandstone(OptionalVariantBlock[SandType]):
    id = 'sandstone'

    @dataclass
    class Chiseled(OptionalVariantBlock[SandType]):
        id = 'sandstone'
        prefix = 'chiseled'

    @dataclass
    class Cut(OptionalVariantBlock[SandType]):
        id = 'sandstone'
        prefix = 'cut'


@dataclass
class Sapling(VariantBlock[StandardTree]):
    id = 'sapling'

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
class ShulkerBox(OptionalVariantBlock[Color]):
    id = 'shulker_box'

    facing: Direction | None = None


@dataclass
class Sign(Waterloggable, VariantBlock[WoodType]):
    id = 'sign'

    rotation: Nibble | None = None

    @dataclass
    class Hanging(Waterloggable, VariantBlock[WoodType]):
        id = 'hanging_sign'

        attached: bool | None = None
        rotation: Nibble | None = None

        @dataclass
        class Wall(Waterloggable, VariantBlock[WoodType]):
            id = 'wall_hanging_sign'

            facing: HorizontalDirection | None = None

    @dataclass
    class Wall(Waterloggable, VariantBlock[WoodType]):
        id = 'wall_sign'

        facing: HorizontalDirection | None = None


@dataclass
class Slab(Waterloggable, VariantBlock[SlabBlock]):
    id = 'slab'

    type: Half | Literal['double'] | None = None


@dataclass
class Stairs(Waterloggable, VariantBlock[SlabStairsBlock]):
    id = 'stairs'

    facing: HorizontalDirection | None = None
    half: Half | None = None
    shape: (
        Literal['inner_left', 'inner_right', 'outer_left', 'outer_right', 'straight']
        | None
    ) = None


class Stem:
    @dataclass
    class Crop(VariantBlock[StemBlock]):
        id = 'stem'

        age: Literal[0, 1, 2, 3, 4, 5, 6, 7] | None = None

        @dataclass
        class Attached(VariantBlock[StemBlock]):
            id = 'stem'
            prefix = 'attached'

            facing: HorizontalDirection | None = None

    @dataclass
    class Fungus(VariantBlock[FungusType]):
        id = 'stem'

        axis: Axis | None = None


@dataclass
class Stone(MinecraftBlock):
    id = 'stone'

    @dataclass
    class Bricks(OptionalVariantBlock[Literal['chiseled', 'cracked']]):
        id = 'stone_bricks'


@dataclass
class Terracotta(OptionalVariantBlock[Color]):
    id = 'terracotta'

    @dataclass
    class Glazed(VariantBlock[Color]):
        id = 'glazed_terracotta'

        facing: HorizontalDirection | None = None


@dataclass
class Trapdoor(Waterloggable, VariantBlock[WoodType]):
    id = 'trapdoor'

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
class Wall(Waterloggable, VariantBlock[StoneType]):
    id = 'wall'

    east: WallHeight | None = None
    north: WallHeight | None = None
    south: WallHeight | None = None
    up: bool | None = None
    west: WallHeight | None = None


@dataclass
class Wood(VariantBlock[Tree]):
    id = 'wood'

    axis: Axis | None = None


@dataclass
class Wool(VariantBlock[Color]):
    id = 'wool'
