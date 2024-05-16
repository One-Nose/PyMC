from pytest import fixture

from src.command import Kill, Teleport
from src.context import Context
from src.datapack import DataPack
from src.entity import Entity
from src.function import Function
from src.position import Position, PositionedAs, RelativePosition
from src.resource_path import ResourcePath


@fixture
def entity() -> Entity:
    return Entity()


@fixture
def position() -> Position:
    return Position()


@fixture
def context(entity, position) -> Context:
    return Context(entity=entity, position=position)


@fixture
def func(context) -> Function:
    return Function(
        DataPack('test'),
        ResourcePath('foo', 'bar'),
        context,
    )


@fixture
def positioned_as_entity(entity) -> PositionedAs:
    return PositionedAs(entity)


@fixture
def relative_position(position) -> RelativePosition:
    return RelativePosition(position, (0, +1, -2))


@fixture
def below_entity(positioned_as_entity) -> RelativePosition:
    return RelativePosition(positioned_as_entity, (0, -1, 0))


@fixture
def kill(entity) -> Kill:
    return Kill(entity)


@fixture
def teleport(entity, position) -> Teleport:
    return Teleport(entity, position)
