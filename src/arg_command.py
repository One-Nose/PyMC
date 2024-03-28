from __future__ import annotations

from typing import TYPE_CHECKING

from .command import Command

if TYPE_CHECKING:
    from .argument import Argument


class ArgCommand(Command):
    arguments: list[str | Argument]

    def __init__(self, *arguments: str | Argument) -> None:
        self.arguments = list(arguments)

    def get_args(self) -> list[str | Argument]:
        return self.arguments
