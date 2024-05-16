from .resource_path import ResourceLocation, ResourceLocationLike


class Block:
    id: ResourceLocation
    block_states: dict[str, str]

    def __init__(self, id: ResourceLocationLike, block_states: dict[str, str]) -> None:
        self.id = ResourceLocation(id)
        self.block_states = block_states

    def to_string(self) -> str:
        if len(self.block_states) == 0:
            return str(self.id)

        return (
            f'{self.id}['
            + ', '.join(
                f'{state}={value}' for state, value in self.block_states.items()
            )
            + ']'
        )
