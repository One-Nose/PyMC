from tests.fixtures import *


def test_to_string(func, kill, teleport):
    func.add(kill)
    func.add(teleport)
    assert func.to_string() == 'kill @s\n' 'teleport @s ~ ~ ~'
