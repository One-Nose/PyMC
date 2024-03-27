from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING, Any, ClassVar, Self

if TYPE_CHECKING:
    from .command import Command
    from .datapack import DataPack
    from .entity import Entity


class Context:
    _stack: ClassVar[deque[Context]] = deque()

    @classmethod
    def get(cls) -> Context:
        return cls._stack[-1]

    datapack: DataPack
    commands: list[Command]
    entity: Entity | None

    def __init__(self, datapack: DataPack, entity: Entity | None) -> None:
        self.datapack = datapack
        self.commands = []
        self.entity = entity

    def __enter__(self) -> Self:
        self.enter()
        return self

    def __exit__(self, exc_type: Exception | None, *_: Any) -> bool:
        self.exit()
        return exc_type is None

    def enter(self) -> None:
        self._stack.append(self)

    def exit(self) -> None:
        Context._stack.pop()

    def to_string(self) -> str:
        text = ''
        for command in self.commands:
            text += command.to_string(self.entity) + '\n'
        return text
