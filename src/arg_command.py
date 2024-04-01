from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING

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

    def get_mark_arguments(self) -> Iterator[Argument]:
        return (
            argument for argument in self.arguments if not isinstance(argument, str)
        )

    def args_list(self) -> list[str]:
        return [repr(arg) for arg in self.arguments]
