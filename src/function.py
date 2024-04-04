from .command import Command
from .context import Context
from .resource_path import ResourcePath


class Function:
    _path: ResourcePath
    _context: Context

    _commands: list[Command]

    def __init__(self, path: ResourcePath, context: Context) -> None:
        self._path = path
        self._context = context

        self._commands = []

    def add(self, command: Command) -> None:
        self._commands.append(command)

    def to_string(self) -> str:
        return '\n'.join(command.to_string(self._context) for command in self._commands)
