from pathlib import Path

from src.command import Kill, Teleport
from src.function import Function


def test_to_string(func: Function, kill: Kill, teleport: Teleport):
    func.add(kill)
    func.add(teleport)
    assert func.to_string() == 'kill @s\n' 'teleport @s ~ ~ ~'


def test_inner_path(func: Function):
    assert func.inner_path() == Path('function/foo/bar')
