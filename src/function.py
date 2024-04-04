from .command import Command, FunctionCommand
from .context import Context
from .datapack import DataPack
from .resource_path import ResourcePath


class Function:
    _datapack: DataPack
    _path: ResourcePath
    _context: Context

    _commands: list[Command]

    def __init__(
        self, datapack: DataPack, path: ResourcePath, context: Context
    ) -> None:
        self._datapack = datapack
        self._path = path
        self._context = context

        self._commands = []

    def add(self, command: Command) -> None:
        self._commands.append(command)

    def to_string(self) -> str:
        return '\n'.join(command.to_string(self._context) for command in self._commands)

    def to_command(self, context: Context) -> FunctionCommand:
        assert context.applies_to_template(self._context)
        return FunctionCommand(context, self)

    def name(self) -> str:
        return self._path.namespaced(self._datapack.namespace)
