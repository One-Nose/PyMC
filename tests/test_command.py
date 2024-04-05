from pytest import raises

from src.command import Kill, Teleport
from src.context import Context
from src.entity import Entity
from src.exception import BadFunctionCall, ContextCombineError, FlatteningError
from tests.fixtures import *


def test_kill(context, kill):
    assert kill.to_string(context) == 'kill @s'


def test_teleport(context, teleport):
    assert teleport.to_string(context) == 'teleport @s ~ ~ ~'


def test_teleport_positioned_as(context, entity, positioned_as_entity):
    assert (
        Teleport(entity, positioned_as_entity).to_string(context)
        == 'execute positioned as @s run teleport @s ~ ~ ~'
    )


def test_relative_position(context, entity, relative_position):
    assert (
        Teleport(entity, relative_position).to_string(context) == 'teleport @s ~ ~1 ~-2'
    )


def test_teleport_below_entity(context, entity, below_entity):
    assert (
        Teleport(entity, below_entity).to_string(context)
        == 'execute positioned as @s run teleport @s ~ ~-1 ~'
    )


def test_function(func, context, entity, position):
    assert (
        func.to_command(Context(entity=entity, position=position)).to_string(context)
        == 'function test:foo/bar'
    )


def test_bad_function_call(func, entity):
    with raises(BadFunctionCall):
        func.to_command(Context(entity=entity))


def test_function_positioned(func, context, entity, relative_position):
    assert (
        func.to_command(
            Context(
                entity=entity,
                position=relative_position.as_provider(),
            )
        ).to_string(context)
        == 'execute positioned ~ ~1 ~-2 run function test:foo/bar'
    )


def test_function_below_entity(func, context, entity, below_entity):
    assert func.to_command(
        Context(entity=entity, position=below_entity.as_provider())
    ).to_string(context) == (
        'execute positioned as @s positioned ~ ~-1 ~ run function test:foo/bar'
    )


def test_kill_bad_entity(context):
    with raises(FlatteningError):
        Kill(Entity()).to_string(context)


def test_context_combine_error(context):
    with raises(ContextCombineError):
        Context.combine(context, Context(entity=Entity()))
