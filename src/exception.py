class MinecraftException(Exception):
    pass


class BadFunctionSignature(MinecraftException):
    pass


class IncompatibleEntity(MinecraftException):
    pass


class IncompatiblePosition(MinecraftException):
    pass


class InvalidResourcePath(MinecraftException):
    def __init__(self, path: str) -> None:
        super().__init__(f'resource path {path!r} is invalid')


class InvalidResourceString(MinecraftException):
    def __init__(self, string: str) -> None:
        super().__init__(f'resource string {str!r} is invalid')
