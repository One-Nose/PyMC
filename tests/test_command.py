from pytest import raises

from src.block import block
from src.command import Kill, SetBlock, Teleport
from src.context import Context
from src.entity import Entity, EveryEntity
from src.exception import BadFunctionCall, ContextCombineError, FlatteningError
from src.function import Function
from src.position import AbsolutePosition, Position, PositionedAs, RelativePosition


def test_kill(context: Context, kill: Kill):
    assert kill.to_string(context) == 'kill @s'


def test_teleport(context: Context, teleport: Teleport):
    assert teleport.to_string(context) == 'teleport @s ~ ~ ~'


def test_teleport_positioned_as(
    context: Context, entity: Entity, positioned_as_entity: PositionedAs
):
    assert (
        Teleport(entity, positioned_as_entity).to_string(context)
        == 'execute positioned as @s run teleport @s ~ ~ ~'
    )


def test_relative_position(
    context: Context, entity: Entity, relative_position: RelativePosition
):
    assert (
        Teleport(entity, relative_position).to_string(context) == 'teleport @s ~ ~1 ~-2'
    )


def test_semi_relative_position(
    context: Context, entity: Entity, semi_relative_position: RelativePosition
):
    assert (
        Teleport(entity, semi_relative_position).to_string(context)
        == 'teleport @s 3 ~ ~-1'
    )


def test_teleport_below_entity(
    context: Context, entity: Entity, below_entity: RelativePosition
):
    assert (
        Teleport(entity, below_entity).to_string(context)
        == 'execute positioned as @s run teleport @s ~ ~-1 ~'
    )


def test_function(func: Function, context: Context, entity: Entity, position: Position):
    assert (
        func.to_command(Context(entity=entity, position=position)).to_string(context)
        == 'function test:foo/bar'
    )


def test_bad_function_call(func: Function, entity: Entity):
    with raises(BadFunctionCall):
        func.to_command(Context(entity=entity))


def test_function_positioned(
    func: Function,
    context: Context,
    entity: Entity,
    relative_position: RelativePosition,
):
    assert (
        func.to_command(
            Context(
                entity=entity,
                position=relative_position.as_provider(),
            )
        ).to_string(context)
        == 'execute positioned ~ ~1 ~-2 run function test:foo/bar'
    )


def test_function_below_entity(
    func: Function, context: Context, entity: Entity, below_entity: RelativePosition
):
    assert func.to_command(
        Context(entity=entity, position=below_entity.as_provider())
    ).to_string(context) == (
        'execute positioned as @s positioned ~ ~-1 ~ run function test:foo/bar'
    )


def test_kill_bad_entity(context: Context):
    with raises(FlatteningError):
        Kill(Entity()).to_string(context)


def test_context_combine_error(context: Context):
    with raises(ContextCombineError):
        Context.combine(context, Context(entity=Entity()))


def test_set_block(context: Context, position: Position):
    assert (
        SetBlock(position, block('cave_air')).to_string(context)
        == 'setblock ~ ~ ~ minecraft:cave_air'
    )


def test_set_block_below(context: Context, below_entity: RelativePosition):
    assert (
        SetBlock(below_entity, block('andesite')).to_string(context)
        == 'execute positioned as @s run setblock ~ ~-1 ~ minecraft:andesite'
    )


def test_place_planks(context: Context, position: Position):
    assert (
        SetBlock(position, block('oak_planks')).to_string(context)
        == 'setblock ~ ~ ~ minecraft:oak_planks'
    )


def test_block_state(context: Context, position: Position):
    assert (
        SetBlock(position, block('bamboo_door', open=False, facing='north')).to_string(
            context
        )
        == 'setblock ~ ~ ~ minecraft:bamboo_door[open=false, facing=north]'
    )


def test_ascending_rail(context: Context, position: Position):
    assert (
        SetBlock(position, block('activator_rail', shape='ascending_south')).to_string(
            context
        )
        == 'setblock ~ ~ ~ minecraft:activator_rail[shape=ascending_south]'
    )


def test_attached_stem(context: Context, position: Position):
    assert (
        SetBlock(position, block('attached_melon_stem')).to_string(context)
        == 'setblock ~ ~ ~ minecraft:attached_melon_stem'
    )


def test_shulker_box(context: Context, position: Position):
    assert (
        SetBlock(position, block('shulker_box')).to_string(context)
        == 'setblock ~ ~ ~ minecraft:shulker_box'
    )


def test_facing_shulker_box(context: Context, position: Position):
    assert (
        SetBlock(position, block('shulker_box', facing='east')).to_string(context)
        == 'setblock ~ ~ ~ minecraft:shulker_box[facing=east]'
    )


def test_black_shulker_box(context: Context, position: Position):
    assert (
        SetBlock(position, block('black_shulker_box')).to_string(context)
        == 'setblock ~ ~ ~ minecraft:black_shulker_box'
    )


def test_glass_pane(context: Context, position: Position):
    assert (
        SetBlock(position, block('glass_pane', south=False)).to_string(context)
        == 'setblock ~ ~ ~ minecraft:glass_pane[south=false]'
    )


def test_stained_glass_pane(context: Context, position: Position):
    assert (
        SetBlock(position, block('black_stained_glass_pane', west=True)).to_string(
            context
        )
        == 'setblock ~ ~ ~ minecraft:black_stained_glass_pane[west=true]'
    )


def test_kill_everybody():
    assert Kill(EveryEntity()).to_string(Context()) == 'kill @e'


def test_func_everybody(func: Function, context: Context, position: Position):
    assert (
        func.to_command(
            Context(entity=EveryEntity().as_provider(), position=position)
        ).to_string(context)
        == 'execute as @e run function test:foo/bar'
    )


def test_absolute_position():
    assert (
        SetBlock(
            AbsolutePosition((0, -10, 20)), block('green_bed', facing='east')
        ).to_string(Context())
        == 'setblock 0 -10 20 minecraft:green_bed[facing=east]'
    )
