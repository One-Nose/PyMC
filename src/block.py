from collections.abc import Generator
from dataclasses import dataclass, field, fields

from .resource_path import ResourceLocation


@dataclass
class Block:
    block_id: ResourceLocation = field(init=False, metadata={'is_state': False})

    def block_states(self) -> Generator[str, None, None]:
        for field in fields(self):
            if field.metadata.get('is_state', True):
                yield field.name

    def to_string(self) -> str:
        block_states: dict[str, str] = {}

        for state in self.block_states():
            value = getattr(self, state)
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
