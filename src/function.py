from .command import Command, FunctionCommand
from .context import Context
from .datapack import DataPack
from .exception import BadFunctionCall
from .resource_path import ResourceLocation, ResourcePath


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
        if not context.applies_to_template(self._context):
            raise BadFunctionCall
        return FunctionCommand(context, self)

    def namespaced(self) -> ResourceLocation:
        return ResourceLocation(self._datapack.namespace, self._path)
