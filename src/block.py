from __future__ import annotations

from typing import Literal, overload

from .block_class import Block

type Direction = HorizontalDirection | Literal['down', 'up']
type HorizontalDirection = Literal['east', 'north', 'south', 'west']
type StraightRailShape = Literal[
    'ascending_east',
    'ascending_north',
    'ascending_south',
    'ascending_west',
    'east_west',
    'north_south',
]
type NaturalNumberBelow4 = Literal[0, 1, 2, 3]
type NaturalNumberBelow6 = NaturalNumberBelow4 | Literal[4, 5]
type NaturalNumberBelow7 = NaturalNumberBelow6 | Literal[6]
type NaturalNumberBelow8 = NaturalNumberBelow7 | Literal[7]
type NaturalNumberBelow9 = NaturalNumberBelow8 | Literal[8]
type NaturalNumberBelow16 = NaturalNumberBelow9 | Literal[9, 10, 11, 12, 13, 14, 15]
type NaturalNumberBelow25 = NaturalNumberBelow16 | Literal[
    16, 17, 18, 19, 20, 21, 22, 23, 24
]
type NaturalNumberBelow26 = NaturalNumberBelow25 | Literal[25]
type WallHeight = Literal['low', 'none', 'high']


@overload
def block(
    id: Literal[
        'acacia_button',
        'bamboo_button',
        'birch_button',
        'cherry_button',
        'crimson_button',
        'dark_oak_button',
        'jungle_button',
        'lever',
        'mangrove_button',
        'oak_button',
        'spruce_button',
        'warped_button',
    ],
    *,
    face: Literal['ceiling', 'floor', 'wall'] = ...,
    facing: HorizontalDirection = ...,
    powered: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'acacia_door',
        'bamboo_door',
        'birch_door',
        'cherry_door',
        'crimson_door',
        'dark_oak_door',
        'iron_door',
        'jungle_door',
        'mangrove_door',
        'oak_door',
        'spruce_door',
        'warped_door',
    ],
    *,
    facing: HorizontalDirection = ...,
    half: Literal['lower', 'upper'] = ...,
    hinge: Literal['left', 'right'] = ...,
    open: bool = ...,
    powered: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'acacia_fence',
        'bamboo_fence',
        'birch_fence',
        'black_stained_glass_pane',
        'blue_stained_glass_pane',
        'brown_stained_glass_pane',
        'cherry_fence',
        'crimson_fence',
        'cyan_stained_glass_pane',
        'dark_oak_fence',
        'glass_pane',
        'gray_stained_glass_pane',
        'green_stained_glass_pane',
        'iron_bars',
        'jungle_fence',
        'light_blue_stained_glass_pane',
        'light_gray_stained_glass_pane',
        'lime_stained_glass_pane',
        'magenta_stained_glass_pane',
        'mangrove_fence',
        'nether_brick_fence',
        'oak_fence',
        'orange_stained_glass_pane',
        'pink_stained_glass_pane',
        'purple_stained_glass_pane',
        'red_stained_glass_pane',
        'spruce_fence',
        'warped_fence',
        'white_stained_glass_pane',
        'yellow_stained_glass_pane',
    ],
    *,
    east: bool = ...,
    north: bool = ...,
    south: bool = ...,
    waterlogged: bool = ...,
    west: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'acacia_fence_gate',
        'bamboo_fence_gate',
        'birch_fence_gate',
        'cherry_fence_gate',
        'crimson_fence_gate',
        'dark_oak_fence_gate',
        'jungle_fence_gate',
        'mangrove_fence_gate',
        'oak_fence_gate',
        'spruce_fence_gate',
        'warped_fence_gate',
    ],
    *,
    facing: HorizontalDirection = ...,
    in_wall: bool = ...,
    open: bool = ...,
    powered: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'acacia_hanging_sign',
        'bamboo_hanging_sign',
        'birch_hanging_sign',
        'cherry_hanging_sign',
        'crimson_hanging_sign',
        'dark_oak_hanging_sign',
        'jungle_hanging_sign',
        'mangrove_hanging_sign',
        'oak_hanging_sign',
        'spruce_hanging_sign',
        'warped_hanging_sign',
    ],
    *,
    attached: bool = ...,
    rotation: NaturalNumberBelow16 = ...,
    waterlogged: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'acacia_leaves',
        'azalea_leaves',
        'birch_leaves',
        'cherry_leaves',
        'dark_oak_leaves',
        'flowering_azalea_leaves',
        'jungle_leaves',
        'mangrove_leaves',
        'oak_leaves',
        'spruce_leaves',
    ],
    *,
    distance: Literal[1, 2, 3, 4, 5, 6, 7] = ...,
    persistent: bool = ...,
    waterlogged: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'acacia_log',
        'acacia_wood',
        'bamboo_block',
        'basalt',
        'birch_log',
        'birch_wood',
        'bone_block',
        'cherry_log',
        'cherry_wood',
        'crimson_hyphae',
        'crimson_stem',
        'dark_oak_log',
        'dark_oak_wood',
        'deepslate',
        'hay_block',
        'jungle_log',
        'jungle_wood',
        'mangrove_log',
        'mangrove_wood',
        'muddy_mangrove_roots',
        'oak_log',
        'oak_wood',
        'ochre_froglight',
        'pearlescent_froglight',
        'spruce_log',
        'spruce_wood',
        'verdant_froglight',
        'warped_hyphae',
        'warped_stem',
    ],
    *,
    axis: Literal['x', 'y', 'z'] = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'acacia_presure_plate',
        'bamboo_presure_plate',
        'birch_presure_plate',
        'cherry_presure_plate',
        'crimson_presure_plate',
        'dark_oak_presure_plate',
        'jungle_presure_plate',
        'mangrove_presure_plate',
        'oak_presure_plate',
        'spruce_presure_plate',
        'warped_presure_plate',
    ],
    *,
    powered: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'acacia_sapling',
        'birch_sapling',
        'cherry_sapling',
        'dark_oak_sapling',
        'jungle_sapling',
        'oak_sapling',
        'spruce_sapling',
    ],
    *,
    stage: Literal[0, 1],
) -> Block: ...


@overload
def block(
    id: Literal[
        'acacia_sign',
        'bamboo_sign',
        'birch_sign',
        'cherry_sign',
        'crimson_sign',
        'dark_oak_sign',
        'jungle_sign',
        'mangrove_sign',
        'oak_sign',
        'spruce_sign',
        'warped_sign',
    ],
    *,
    rotation: NaturalNumberBelow16 = ...,
    waterlogged: NaturalNumberBelow16 = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'acacia_slab',
        'andesite_slab',
        'bamboo_slab',
        'bamboo_mosaic_slab',
        'birch_slab',
        'blackstone_slab',
        'brick_slab',
        'cherry_slab',
        'cobbled_deepslate_slab',
        'cobblestone_slab',
        'crimson_slab',
        'cut_copper_slab',
        'cut_red_sandstone_slab',
        'cut_sandstone_slab',
        'dark_oak_slab',
        'dark_prismarine_slab',
        'deepslate_brick_slab',
        'deepslate_tile_slab',
        'diorite_slab',
        'end_stone_brick_slab',
        'exposed_cut_copper_slab',
        'granite_slab',
        'jungle_slab',
        'mangrove_slab',
        'mossy_cobblestone_slab',
        'mossy_stone_brick_slab',
        'mud_brick_slab',
        'nether_brick_slab',
        'oak_slab',
        'oxidized_cut_copper_slab',
        'polished_andesite_slab',
        'polished_blackstone_brick_slab',
        'polished_blackstone_slab',
        'polished_deepslate_slab',
        'polished_diorite_slab',
        'polished_granite_slab',
        'prismarine_brick_slab',
        'prismarine_slab',
        'purpur_slab',
        'quartz_slab',
        'red_nether_brick_slab',
        'red_sandstone_slab',
        'sandstone_slab',
        'smooth_quartz_slab',
        'smooth_red_sandstone_slab',
        'smooth_sandstone_slab',
        'smooth_stone_slab',
        'spruce_slab',
        'stone_brick_slab',
        'stone_slab',
        'warped_slab',
        'waxed_cut_copper_slab',
        'waxed_exposed_cut_copper_slab',
        'waxed_oxidized_cut_copper_slab',
        'waxed_cut_copper_slab',
        'waxed_weathered_cut_copper_slab',
        'weathered_cut_copper_slab',
    ],
    *,
    type: Literal['bottom', 'double', 'top'] = ...,
    waterlogged: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'acacia_stairs',
        'andesite_stairs',
        'bamboo_stairs',
        'bamboo_mosaic_stairs',
        'birch_stairs',
        'blackstone_stairs',
        'brick_stairs',
        'cherry_stairs',
        'cobbled_deepslate_stairs',
        'cobblestone_stairs',
        'crimson_stairs',
        'cut_copper_stairs',
        'dark_oak_stairs',
        'dark_prismarine_stairs',
        'deepslate_brick_stairs',
        'deepslate_tile_stairs',
        'diorite_stairs',
        'end_stone_brick_stairs',
        'exposed_cut_copper_stairs',
        'granite_stairs',
        'jungle_stairs',
        'mangrove_stairs',
        'mossy_cobblestone_stairs',
        'mossy_stone_brick_stairs',
        'mud_brick_stairs',
        'nether_brick_stairs',
        'oak_stairs',
        'oxidized_cut_copper_stairs',
        'polished_andesite_stairs',
        'polished_blackstone_brick_stairs',
        'polished_blackstone_stairs',
        'polished_deepslate_stairs',
        'polished_diorite_stairs',
        'polished_granite_stairs',
        'prismarine_brick_stairs',
        'prismarine_stairs',
        'purpur_stairs',
        'quartz_stairs',
        'red_nether_brick_stairs',
        'red_sandstone_stairs',
        'sandstone_stairs',
        'smooth_quartz_stairs',
        'smooth_red_sandstone_stairs',
        'smooth_sandstone_stairs',
        'spruce_stairs',
        'stone_brick_stairs',
        'stone_stairs',
        'warped_stairs',
        'waxed_cut_copper_stairs',
        'waxed_exposed_cut_copper_stairs',
        'waxed_oxidized_cut_copper_stairs',
        'waxed_weathered_cut_copper_stairs',
        'weathered_cut_copper_stairs',
    ],
    *,
    facing: HorizontalDirection = ...,
    half: Literal['bottom', 'top'] = ...,
    shape: Literal[
        'inner_left', 'inner_right', 'outer_left', 'outer_right', 'straight'
    ] = ...,
    waterlogged: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'acacia_trapdoor',
        'bamboo_trapdoor',
        'birch_trapdoor',
        'cherry_trapdoor',
        'crimson_trapdoor',
        'dark_oak_trapdoor',
        'iron_trapdoor',
        'jungle_trapdoor',
        'mangrove_trapdoor',
        'oak_trapdoor',
        'spruce_trapdoor',
        'warped_trapdoor',
    ],
    *,
    facing: HorizontalDirection = ...,
    half: Literal['bottom', 'top'] = ...,
    open: bool = ...,
    powered: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'acacia_wall_hanging_sign',
        'acacia_wall_sign',
        'bamboo_wall_hanging_sign',
        'bamboo_wall_sign',
        'big_dripleaf_stem',
        'birch_wall_hanging_sign',
        'birch_wall_sign',
        'brain_coral_wall_fan',
        'bubble_coral_wall_fan',
        'cherry_wall_hanging_sign',
        'cherry_wall_sign',
        'crimson_wall_hanging_sign',
        'crimson_wall_sign',
        'dark_oak_wall_hanging_sign',
        'dark_oak_wall_sign',
        'dead_brain_coral_wall_fan',
        'dead_bubble_coral_wall_fan',
        'dead_fire_coral_wall_fan',
        'dead_horn_coral_wall_fan',
        'dead_tube_coral_wall_fan',
        'ender_chest',
        'fire_coral_wall_fan',
        'horn_coral_wall_fan',
        'jungle_wall_hanging_sign',
        'jungle_wall_sign',
        'ladder',
        'mangrove_wall_hanging_sign',
        'mangrove_wall_sign',
        'oak_wall_hanging_sign',
        'oak_wall_sign',
        'spruce_wall_hanging_sign',
        'spruce_wall_sign',
        'tube_coral_wall_fan',
        'warped_wall_hanging_sign',
        'warped_wall_sign',
    ],
    *,
    facing: HorizontalDirection = ...,
    waterlogged: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal['activator_rail', 'detector_rail'],
    *,
    powered: bool = ...,
    shape: StraightRailShape = ...,
    waterlogged: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal['amethyst_cluster', 'large_amethyst_bud', 'medium_amethyst_bud'],
    *,
    facing: Direction = ...,
    waterlogged: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'andesite_wall',
        'blackstone_wall',
        'brick_wall',
        'cobbled_deepslate_wall',
        'cobblestone_wall',
        'deepslate_brick_wall',
        'deepslate_tile_wall',
        'diorite_wall',
        'end_stone_brick_wall',
        'granite_wall',
        'mossy_cobblestone_wall',
        'mossy_stone_brick_wall',
        'mud_brick_wall',
        'nether_brick_wall',
    ],
    *,
    east: WallHeight = ...,
    north: WallHeight = ...,
    south: WallHeight = ...,
    up: bool = ...,
    waterlogged: bool = ...,
    west: WallHeight = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'anvil',
        'attached_melon_stem',
        'black_glazed_terracotta',
        'black_wall_banner',
        'blue_glazed_terracotta',
        'blue_wall_banner',
        'brown_glazed_terracotta',
        'brown_wall_banner',
        'carved_pumpkin',
        'chipped_anvil',
        'cyan_glazed_terracotta',
        'cyan_wall_banner',
        'damaged_anvil',
        'gray_glazed_terracotta',
        'gray_wall_banner',
        'green_glazed_terracotta',
        'green_wall_banner',
        'jack_o_lantern',
        'light_blue_glazed_terracotta',
        'light_blue_wall_banner',
        'light_gray_glazed_terracotta',
        'light_gray_wall_banner',
        'lime_glazed_terracotta',
        'lime_wall_banner',
        'loom',
        'magenta_glazed_terracotta',
        'magenta_wall_banner',
        'orange_glazed_terracotta',
        'orange_wall_banner',
        'pink_glazed_terracotta',
        'pink_wall_banner',
        'purple_glazed_terracotta',
        'purple_wall_banner',
        'red_glazed_terracotta',
        'red_wall_banner',
        'white_glazed_terracotta',
        'white_wall_banner',
        'yellow_glazed_terracotta',
        'yellow_wall_banner',
    ],
    *,
    facing: HorizontalDirection = ...,
) -> Block: ...


@overload
def block(
    id: Literal['bamboo'],
    *,
    age: Literal[0, 1] = ...,
    leaves: Literal['large', 'none', 'small'] = ...,
    stage: Literal[0, 1] = ...,
) -> Block: ...


@overload
def block(
    id: Literal['barrel'], *, facing: Direction = ..., open: bool = ...
) -> Block: ...


@overload
def block(
    id: Literal[
        'barrier',
        'brain_coral',
        'brain_coral_fan',
        'bubble_coral',
        'bubble_coral_fan',
        'conduit',
        'dead_brain_coral',
        'dead_brain_coral_fan',
        'dead_bubble_coral',
        'dead_bubble_coral_fan',
        'dead_fire_coral',
        'dead_fire_coral_fan',
        'dead_horn_coral',
        'dead_horn_coral_fan',
        'dead_tube_coral',
        'dead_tube_coral_fan',
        'fire_coral',
        'fire_coral_fan',
        'horn_coral',
        'horn_coral_fan',
        'mangrove_roots',
        'tube_coral',
        'tube_coral_fan',
    ],
    *,
    waterlogged: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal['bee_nest', 'beehive'],
    *,
    facing: HorizontalDirection = ...,
    honey_level: NaturalNumberBelow6 = ...,
) -> Block: ...


@overload
def block(
    id: Literal['beetroots', 'frosted_ice', 'nether_wart'],
    *,
    age: NaturalNumberBelow4 = ...,
) -> Block: ...


@overload
def block(
    id: Literal['bell'],
    *,
    attachment: Literal['ceiling', 'double_wall', 'floor', 'single_wall'] = ...,
    facing: HorizontalDirection = ...,
    powered: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal['big_dripleaf'],
    *,
    facing: HorizontalDirection = ...,
    tilt: Literal['full', 'none', 'partial', 'unstable'] = ...,
    waterlogged: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'black_banner',
        'blue_banner',
        'brown_banner',
        'cyan_banner',
        'gray_banner',
        'green_banner',
        'light_blue_banner',
        'light_gray_banner',
        'lime_banner',
        'magenta_banner',
        'orange_banner',
        'pink_banner',
        'purple_banner',
        'red_banner',
        'white_banner',
        'yellow_banner',
    ],
    *,
    rotation: NaturalNumberBelow16 = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'black_bed',
        'blue_bed',
        'brown_bed',
        'cyan_bed',
        'gray_bed',
        'green_bed',
        'light_blue_bed',
        'light_gray_bed',
        'lime_bed',
        'magenta_bed',
        'orange_bed',
        'pink_bed',
        'purple_bed',
        'red_bed',
        'white_bed',
        'yellow_bed',
    ],
    *,
    facing: HorizontalDirection = ...,
    occupied: bool = ...,
    part: Literal['foot', 'head'] = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'black_candle',
        'blue_candle',
        'brown_candle',
        'candle',
        'cyan_candle',
        'gray_candle',
        'green_candle',
        'light_blue_candle',
        'light_gray_candle',
        'lime_candle',
        'magenta_candle',
        'orange_candle',
        'pink_candle',
        'purple_candle',
        'red_candle',
        'white_candle',
        'yellow_candle',
    ],
    *,
    candles: Literal[1, 2, 3, 4] = ...,
    lit: bool = ...,
    waterlogged: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'black_candle_cake',
        'blue_candle_cake',
        'brown_candle_cake',
        'candle_cake',
        'cyan_candle_cake',
        'deepslate_redstone_ore',
        'gray_candle_cake',
        'green_candle_cake',
        'light_blue_candle_cake',
        'light_gray_candle_cake',
        'lime_candle_cake',
        'magenta_candle_cake',
        'orange_candle_cake',
        'pink_candle_cake',
        'purple_candle_cake',
        'red_candle_cake',
        'redstone_ore',
        'white_candle_cake',
        'yellow_candle_cake',
    ],
    *,
    lit: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'black_shulker_box',
        'blue_shulker_box',
        'brown_shulker_box',
        'cyan_shulker_box',
        'end_rod',
        'gray_shulker_box',
        'green_shulker_box',
        'light_blue_shulker_box',
        'light_gray_shulker_box',
        'lime_shulker_box',
        'magenta_shulker_box',
        'orange_shulker_box',
        'pink_shulker_box',
        'purple_shulker_box',
        'red_shulker_box',
        'shulker_box',
        'white_shulker_box',
        'yellow_shulker_box',
    ],
    *,
    facing: Direction = ...,
) -> Block: ...


@overload
def block(
    id: Literal['blast_furnace', 'furnace'],
    *,
    facing: HorizontalDirection = ...,
    lit: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal['brewing_stand'],
    *,
    has_bottle_0: bool = ...,
    has_bottle_1: bool = ...,
    has_bottle_2: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal['brown_mushroom_block', 'chorus_plant', 'mushroom_stem'],
    *,
    down: bool = ...,
    east: bool = ...,
    north: bool = ...,
    south: bool = ...,
    up: bool = ...,
    west: bool = ...,
) -> Block: ...


@overload
def block(id: Literal['bubble_column'], *, drag: bool = ...) -> Block: ...


@overload
def block(id: Literal['cactus'], *, age: NaturalNumberBelow16 = ...) -> Block: ...


@overload
def block(id: Literal['cake'], *, bites: NaturalNumberBelow7 = ...) -> Block: ...


@overload
def block(
    id: Literal['calibrated_sculk_sensor'],
    *,
    facing: HorizontalDirection = ...,
    power: NaturalNumberBelow16 = ...,
    sculk_sensor_phase: Literal['active', 'cooldown', 'inactive'] = ...,
    waterlogged: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal['campfire'],
    *,
    facing: HorizontalDirection = ...,
    lit: bool = ...,
    signal_fire: bool = ...,
    waterlogged: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal['carrots', 'melon_stem'], *, age: NaturalNumberBelow8 = ...
) -> Block: ...


@overload
def block(
    id: Literal['cave_vines'],
    *,
    berries: bool = ...,
    age: NaturalNumberBelow26 = ...,
) -> Block: ...


@overload
def block(id: Literal['cave_vines_plant'], *, berries: bool = ...) -> Block: ...


@overload
def block(
    id: Literal['chain'], *, axis: Literal['x', 'y', 'z'] = ..., waterlogged: bool = ...
) -> Block: ...


@overload
def block(
    id: Literal['chain_command_block', 'command_block'],
    *,
    conditional: bool = ...,
    facing: Direction = ...,
) -> Block: ...


@overload
def block(
    id: Literal['chest'],
    *,
    facing: HorizontalDirection = ...,
    type: Literal['left', 'right', 'single'] = ...,
    waterlogged: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal['chiseled_bookshelf'],
    *,
    facing: HorizontalDirection = ...,
    slot_0_occupied: bool = ...,
    slot_1_occupied: bool = ...,
    slot_2_occupied: bool = ...,
    slot_3_occupied: bool = ...,
    slot_4_occupied: bool = ...,
    slot_5_occupied: bool = ...,
) -> Block: ...


@overload
def block(id: Literal['chorus_flower'], *, age: NaturalNumberBelow6 = ...) -> Block: ...


@overload
def block(
    id: Literal['cocoa'],
    *,
    age: Literal[0, 1, 2] = ...,
    facing: HorizontalDirection = ...,
) -> Block: ...


@overload
def block(
    id: Literal['comparator'],
    *,
    facing: HorizontalDirection = ...,
    mode: Literal['compare', 'subtract'] = ...,
    powered: bool = ...,
) -> Block: ...


@overload
def block(id: Literal['composter'], *, level: NaturalNumberBelow9 = ...) -> Block: ...


@overload
def block(
    id: Literal['creeper_head', 'dragon_head'],
    *,
    powered: bool = ...,
    rotation: NaturalNumberBelow16 = ...,
) -> Block: ...


@overload
def block(
    id: Literal['creeper_wall_head', 'dragon_wall_head'],
    *,
    powered: bool = ...,
    facing: HorizontalDirection = ...,
) -> Block: ...


@overload
def block(
    id: Literal['daylight_detector'],
    *,
    inverted: bool = ...,
    power: NaturalNumberBelow16 = ...,
) -> Block: ...


@overload
def block(
    id: Literal['decorated_pot'],
    *,
    facing: HorizontalDirection = ...,
    cracked: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal['dispenser', 'dropper'],
    *,
    facing: Direction = ...,
    triggered: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal['end_portal_frame'],
    *,
    eye: bool = ...,
    facing: HorizontalDirection = ...,
) -> Block: ...


@overload
def block(id: Literal['farmland'], *, moisture: NaturalNumberBelow8 = ...) -> Block: ...


@overload
def block(
    id: Literal['fire'],
    *,
    age: NaturalNumberBelow16 = ...,
    east: bool = ...,
    north: bool = ...,
    south: bool = ...,
    up: bool = ...,
    west: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal['glow_lichen'],
    *,
    down: bool = ...,
    east: bool = ...,
    north: bool = ...,
    south: bool = ...,
    up: bool = ...,
    waterlogged: bool = ...,
    west: bool = ...,
) -> Block: ...


@overload
def block(id: Literal['grass_block', 'mycelium'], *, snowy: bool = ...) -> Block: ...


@overload
def block(
    id: Literal['grindstone'],
    *,
    face: Literal['ceiling', 'floor', 'wall'] = ...,
    facing: HorizontalDirection = ...,
) -> Block: ...


@overload
def block(
    id: Literal['heavy_weighted_pressure_plate', 'light_weighted_pressure_plate'],
    *,
    power: NaturalNumberBelow16 = ...,
) -> Block: ...


@overload
def block(
    id: Literal['hopper'],
    *,
    enabled: bool = ...,
    facing: HorizontalDirection | Literal['down'] = ...,
) -> Block: ...


@overload
def block(
    id: Literal['jigsaw'],
    *,
    orientation: Literal[
        'down_east',
        'down_north',
        'down_south',
        'down_west',
        'east_up',
        'north_up',
        'south_up',
        'up_east',
        'up_north',
        'up_south',
        'up_west',
        'west_up',
    ] = ...,
) -> Block: ...


@overload
def block(id: Literal['jukebox'], *, has_record: bool = ...) -> Block: ...


@overload
def block(id: Literal['kelp'], *, age: NaturalNumberBelow26 = ...) -> Block: ...


@overload
def block(
    id: Literal['lantern'], *, hanging: bool = ..., waterlogged: bool = ...
) -> Block: ...


@overload
def block(
    id: Literal['large_fern', 'lilac'], *, half: Literal['lower', 'upper'] = ...
) -> Block: ...


@overload
def block(id: Literal['lava'], *, level: NaturalNumberBelow16 = ...) -> Block: ...


@overload
def block(
    id: Literal['lectern'],
    *,
    facing: HorizontalDirection = ...,
    has_book: bool = ...,
    powered: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal['light'], *, level: NaturalNumberBelow16 = ..., waterlogged: bool = ...
) -> Block: ...


@overload
def block(
    id: Literal['lightning_rod'],
    *,
    facing: Direction = ...,
    powered: bool = ...,
    waterlogged: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal['mangrove_propagule'],
    *,
    age: NaturalNumberBelow4 = ...,
    hanging: bool = ...,
    stage: Literal[0, 1] = ...,
    waterlogged: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal['moving_piston'],
    *,
    facing: Direction = ...,
    type: Literal['normal', 'sticky'] = ...,
) -> Block: ...


@overload
def block(id: Literal['nether_portal'], *, axis: Literal['x', 'z'] = ...) -> Block: ...


@overload
def block(
    id: Literal['note_block'],
    *,
    instrument: Literal[
        'banjo',
        'basedrum',
        'bass',
        'bell',
        'bit',
        'chime',
        'cow_bell',
        'creeper',
        'custom_head',
        'didgeridoo',
        'dragon',
        'flute',
        'guitar',
        'harp',
        'hat',
        'iron_xylophone',
        'piglin',
        'pling',
        'skeleton',
        'snare',
        'wither_skeleton',
        'xylophone',
        'zombie',
    ] = ...,
    note: NaturalNumberBelow25 = ...,
    powered: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal['observer'], *, facing: Direction = ..., powered: bool = ...
) -> Block: ...


@overload
def block(
    id: Literal['rail'],
    *,
    shape: (
        StraightRailShape
        | Literal['north_east', 'north_west', 'south_east', 'south_west']
    ) = ...,
    waterlogged: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal['sculk_sensor'],
    *,
    power: NaturalNumberBelow16 = ...,
    sculk_sensor_phase: Literal['active', 'cooldown', 'inactive'] = ...,
    waterlogged: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal['vine'],
    *,
    east: bool = ...,
    north: bool = ...,
    south: bool = ...,
    up: bool = ...,
    west: bool = ...,
) -> Block: ...


@overload
def block(
    id: Literal[
        'acacia_planks',
        'air',
        'allium',
        'amethyst_block',
        'ancient_debris',
        'andesite',
        'azalea',
        'azure_bluet',
        'bamboo_mosaic',
        'bamboo_planks',
        'bamboo_sapling',
        'beacon',
        'bedrock',
        'birch_planks',
        'black_carpet',
        'black_concrete',
        'black_concrete_powder',
        'black_stained_glass',
        'black_terracotta',
        'black_wool',
        'blackstone',
        'blue_carpet',
        'blue_concrete',
        'blue_concrete_powder',
        'blue_ice',
        'blue_orchid',
        'blue_stained_glass',
        'blue_terracotta',
        'blue_wool',
        'bookshelf',
        'brain_coral_block',
        'bricks',
        'brown_carpet',
        'brown_concrete',
        'brown_concrete_powder',
        'brown_mushroom',
        'brown_stained_glass',
        'brown_terracotta',
        'brown_wool',
        'bubble_coral_block',
        'budding_amethyst',
        'calcite',
        'cartography_table',
        'cauldron',
        'cave_air',
        'cherry_planks',
        'chiseled_deepslate',
        'chiseled_nether_bricks',
        'chiseled_polished_blackstone',
        'chiseled_quartz_block',
        'chiseled_red_sandstone',
        'chiseled_sandstone',
        'chiseled_stone_bricks',
        'clay',
        'coal_block',
        'coal_ore',
        'coarse_dirt',
        'cobbled_deepslate',
        'cobblestone',
        'cobweb',
        'copper_block',
        'copper_ore',
        'cornflower',
        'cracked_deepslate_bricks',
        'cracked_deepslate_tiles',
        'cracked_nether_bricks',
        'cracked_polished_blackstone',
        'cracked_stone_bricks',
        'crafting_table',
        'crimson_fungus',
        'crimson_nylium',
        'crimson_planks',
        'crimson_roots',
        'crying_obsidian',
        'cut_copper',
        'cut_red_sandstone',
        'cut_sandstone',
        'cyan_carpet',
        'cyan_concrete',
        'cyan_concrete_powder',
        'cyan_stained_glass',
        'cyan_terracotta',
        'cyan_wool',
        'dandelion',
        'dark_oak_planks',
        'dark_prismarine',
        'dead_brain_coral_block',
        'dead_bubble_coral_block',
        'dead_bush',
        'dead_fire_coral_block',
        'dead_horn_coral_block',
        'dead_tube_coral_block',
        'deepslate_bricks',
        'deepslate_tiles',
        'deepslate_coal_ore',
        'deepslate_copper_ore',
        'deepslate_diamond_ore',
        'deepslate_emerald_ore',
        'deepslate_gold_ore',
        'deepslate_iron_ore',
        'deepslate_lapis_ore',
        'diamond_block',
        'diamond_ore',
        'diorite',
        'dirt',
        'dirt_path',
        'dragon_egg',
        'dried_kelp_block',
        'dripstone_block',
        'emerald_block',
        'emerald_ore',
        'enchanting_table',
        'end_gateway',
        'end_portal',
        'end_stone',
        'end_stone_bricks',
        'exposed_copper',
        'exposed_cut_copper',
        'fern',
        'fire_coral_block',
        'fletching_table',
        'flower_pot',
        'flowering_azalea',
        'frogspawn',
        'gilded_blackstone',
        'glass',
        'glowstone',
        'gold_block',
        'gold_ore',
        'granite',
        'gravel',
        'gray_carpet',
        'gray_concrete',
        'gray_concrete_powder',
        'gray_stained_glass',
        'gray_terracotta',
        'gray_wool',
        'green_carpet',
        'green_concrete',
        'green_concrete_powder',
        'green_stained_glass',
        'green_terracotta',
        'green_wool',
        'hanging_roots',
        'honey_block',
        'honeycomb_block',
        'horn_coral_block',
        'ice',
        'infested_chiseled_stone_bricks',
        'infested_cobblestone',
        'infested_cracked_stone_bricks',
        'infested_deepslate',
        'infested_mossy_stone_bricks',
        'infested_stone',
        'infested_stone_bricks',
        'iron_block',
        'iron_ore',
        'jungle_planks',
        'kelp_plant',
        'lapis_block',
        'lapis_ore',
        'lava_cauldron',
        'light_blue_carpet',
        'light_blue_concrete',
        'light_blue_concrete_powder',
        'light_blue_stained_glass',
        'light_blue_terracotta',
        'light_blue_wool',
        'light_gray_carpet',
        'light_gray_concrete',
        'light_gray_concrete_powder',
        'light_gray_stained_glass',
        'light_gray_terracotta',
        'light_gray_wool',
        'lily_of_the_valley',
        'lily_pad',
        'lime_carpet',
        'lime_concrete',
        'lime_concrete_powder',
        'lime_stained_glass',
        'lime_terracotta',
        'lime_wool',
        'lodestone',
        'magenta_carpet',
        'magenta_concrete',
        'magenta_concrete_powder',
        'magenta_stained_glass',
        'magenta_terracotta',
        'magenta_wool',
        'magma_block',
        'mangrove_planks',
        'melon',
        'moss_block',
        'moss_carpet',
        'mossy_cobblestone',
        'mossy_stone_bricks',
        'mud',
        'mud_bricks',
        'nether_bricks',
        'nether_gold_ore',
        'nether_quartz_ore',
        'nether_sprouts',
        'nether_wart_block',
        'netherite_block',
        'netherrack',
        'oak_planks',
        'obsidian',
        'orange_carpet',
        'orange_concrete',
        'orange_concrete_powder',
        'orange_stained_glass',
        'orange_terracotta',
        'orange_tulip',
        'orange_wool',
        'oxeye_daisy',
        'oxidized_copper',
        'oxidized_cut_copper',
        'pink_carpet',
        'pink_concrete',
        'pink_concrete_powder',
        'pink_stained_glass',
        'pink_terracotta',
        'pink_tulip',
        'pink_wool',
        'polished_blackstone',
        'prismarine',
        'pumpkin',
        'purple_carpet',
        'purple_concrete',
        'purple_concrete_powder',
        'purple_stained_glass',
        'purple_terracotta',
        'purple_wool',
        'quartz_block',
        'red_carpet',
        'red_concrete',
        'red_concrete_powder',
        'red_stained_glass',
        'red_terracotta',
        'red_tulip',
        'red_wool',
        'red_sandstone',
        'sandstone',
        'sculk',
        'short_grass',
        'spruce_planks',
        'stone',
        'stone_bricks',
        'terracotta',
        'tube_coral_block',
        'warped_fungus',
        'warped_nylium',
        'warped_planks',
        'warped_roots',
        'waxed_copper_block',
        'waxed_cut_copper',
        'waxed_exposed_copper',
        'waxed_exposed_cut_copper',
        'waxed_oxidized_copper',
        'waxed_oxidized_cut_copper',
        'waxed_weathered_copper',
        'waxed_weathered_cut_copper',
        'weathered_copper',
        'weathered_cut_copper',
        'white_carpet',
        'white_concrete',
        'white_concrete_powder',
        'white_stained_glass',
        'white_terracotta',
        'white_tulip',
        'white_wool',
        'yellow_carpet',
        'yellow_concrete',
        'yellow_concrete_powder',
        'yellow_stained_glass',
        'yellow_terracotta',
        'yellow_wool',
    ]
) -> Block: ...


def block(id: str, **block_states: str | int | bool) -> Block:
    return Block(
        id,
        {name: str(state).lower() for name, state in block_states.items()},
    )
