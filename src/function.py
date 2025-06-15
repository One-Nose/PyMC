from __future__ import annotations

from .command import Command, FunctionCommand
from .context import Context
from .datapack import DataPack
from .exception import BadFunctionCall
from .resource_path import ResourcePathLike
from .resources import Resource


class Function(Resource):
    _resource_type = 'function'

    _context: Context
    _commands: list[Command]

    def __init__(
        self, datapack: DataPack, path: ResourcePathLike, context: Context
    ) -> None:
        super().__init__(datapack, path)

        self._context = context
        self._commands = []

    def to_string(self) -> str:
        return '\n'.join(command.to_string(self._context) for command in self._commands)

    def add(self, command: Command) -> None:
        self._commands.append(command)

    def to_command(self, context: Context) -> FunctionCommand:
        if not context.applies_to_template(self._context):
            raise BadFunctionCall
        return FunctionCommand(context, self)
