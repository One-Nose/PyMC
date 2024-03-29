from __future__ import annotations

from typing import TYPE_CHECKING

from .argument import Argument
from .command import Command

if TYPE_CHECKING:
    from .argument import Argument
    from .entity import Entity
    from .position import Position


class ArgCommand(Command):
    arguments: list[str | Argument]

    def __init__(self, *arguments: str | Argument) -> None:
        self.arguments = list(arguments)

    def to_string(self, entity: Entity | None, position: Position | None) -> str:
        args: list[str] = []

        for arg in self.arguments:
            if isinstance(arg, str):
                args.append(arg)
            else:
                args.append(arg.to_string(entity, position))

        return ' '.join(args)

    def update_mark_commands(self) -> None:
        for arg in self.arguments:
            if isinstance(arg, Argument):
                arg.update_mark_command()

    def args_list(self) -> list[str]:
        return [repr(arg) for arg in self.arguments]
