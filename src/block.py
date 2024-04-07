from dataclasses import dataclass, field
from typing import Any

from .resource_path import ResourceLocation


@dataclass
class Block:
    block_id: ResourceLocation = field(init=False)
    block_states: tuple[str, ...] = field(init=False, default=())

    def to_string(self) -> str:
        block_states: dict[str, str] = {}

        for state in self.block_states:
            value: Any = getattr(self, state)
            if value is not None:
                block_states[state] = str(value).lower()

        if len(block_states) == 0:
            return str(self.block_id)

        return (
            str(self.block_id)
            + '['
            + ', '.join(f'{state}={value}' for state, value in block_states.items())
            + ']'
        )
