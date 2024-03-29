from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Self

from .exception import CommandOutOfContext

if TYPE_CHECKING:
    from .argument import Argument
    from .command import Command
    from .datapack import DataPack
    from .entity import Entity
    from .position import Position


@dataclass
class ArgumentRecord:
    argument: Argument
    number: int
    mark_always: bool


class Context:
    _stack: ClassVar[deque[Context]] = deque()

    @classmethod
    def get(cls) -> Context:
        try:
            return cls._stack[-1]
        except IndexError:
            raise CommandOutOfContext

    datapack: DataPack
    parent: Context | None

    commands: list[Command]
    _arguments: list[ArgumentRecord]

    entity: Entity | None
    position: Position | None

    def __init__(
        self,
        parent: Context | DataPack,
        entity: Entity | None,
        position: Position | None,
    ) -> None:
        if isinstance(parent, Context):
            self.datapack = parent.datapack
            self.parent = parent
        else:
            self.datapack = parent
            self.parent = None

        self.commands = []
        self._arguments = []

        self.entity = entity
        self.position = position

    def add_argument(self, argument: Argument) -> None:
        self._arguments.append(ArgumentRecord(argument, 0, mark_always=False))

    def get_arguments(self) -> list[ArgumentRecord]:
        parent_args = (
            self.parent.get_arguments() if isinstance(self.parent, Context) else []
        )
        return parent_args + self._arguments

    def __enter__(self) -> Self:
        self.enter()
        return self

    def __exit__(self, exc_type: type[BaseException] | None, *_: Any) -> bool:
        self.exit()
        return exc_type is None

    def enter(self) -> None:
        self._stack.append(self)

    def exit(self) -> None:
        for arg in self._arguments:
            if arg.mark_always or arg.number > 1:
                arg.argument.mark()

        Context._stack.pop()

    def to_string(self) -> str:
        text = ''
        for command in self.commands:
            text += command.to_string(self.entity, self.position) + '\n'
        return text
