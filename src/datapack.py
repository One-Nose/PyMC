from __future__ import annotations

from collections.abc import Callable
from functools import wraps
from inspect import signature
from json import dump
from os import makedirs
from os.path import dirname
from pathlib import Path, PurePath
from shutil import rmtree
from typing import Any

from .arg_command import ArgCommand
from .context import Context
from .entity import Entity
from .exception import BadFunctionSignature
from .position import GivenPosition, Position
from .util import ResourceLocation, ResourcePath, ResourceString


class DataPack:
    namespace: ResourceString
    functions: dict[ResourcePath, Function]
    micro_functions: dict[ResourcePath, Context]

    description: str

    def __init__(self, namespace: str, description: str = '') -> None:
        self.namespace = ResourceString(namespace)
        self.functions = {}
        self.micro_functions = {}

        self.description = description

    def compile(self) -> None:
        for function in self.functions.values():
            function.compile()

    def function(self, entity_type: type[Entity] | None = None):
        def wrapper[T: Callable[..., None]](func: T) -> T:
            func_path = ResourcePath(func.__name__)

            self.functions[func_path] = Function(self, func, entity_type)

            @wraps(func)
            def call_func(*args: Any, **kwargs: Any):
                command = ArgCommand('function', self.resource_location(func_path))

                if entity_type is None:
                    command.add()
                else:
                    bound_func = signature(func).bind(*args, **kwargs)
                    bound_func.apply_defaults()
                    with bound_func.args[0]:
                        command.add()

            return call_func  # type: ignore

        return wrapper

    def resource_location(self, path: ResourcePath) -> ResourceLocation:
        return ResourceLocation(self.namespace, path)

    def micro_resource_location(self, path: ResourcePath) -> ResourceLocation:
        return self.resource_location(ResourcePath(f'__pymc/{path}'))

    def generate(self, path: str | PurePath) -> None:
        self.compile()

        path = Path(path)

        try:
            rmtree(path)
        except FileNotFoundError:
            pass

        makedirs(path, exist_ok=True)

        with open(path / 'pack.mcmeta', 'x') as mcmeta:
            dump(
                {'pack': {'description': self.description, 'pack_format': 35}},
                mcmeta,
                indent=2,
            )

        root = path / self.namespace / 'functions'

        func_files: dict[Path, Context] = {}

        for name, func in self.functions.items():
            func_files[root / f'{name}.mcfunction'] = func

        for name, func in self.micro_functions.items():
            func_files[root / '__pymc' / f'{name}.mcfunction'] = func

        for path, func in func_files.items():
            makedirs(dirname(path), exist_ok=True)
            with open(path, 'x') as file:
                file.write(func.to_string())


class Function(Context):
    _func: Callable[..., None]
    _entity_type: type[Entity] | None

    def __init__(
        self,
        datapack: DataPack,
        func: Callable[..., None],
        entity_type: type[Entity] | None,
    ) -> None:
        entity = None if entity_type is None else entity_type()

        args = [] if entity is None else [entity]
        func_signature = signature(func)
        position: GivenPosition | None = None
        try:
            func_signature.bind(*args)
        except TypeError:
            position = GivenPosition()
            try:
                func_signature.bind(*args, position)
            except TypeError:
                raise BadFunctionSignature

        super().__init__(datapack, entity, position)

        self._func = func
        self._entity_type = entity_type

    def compile(self) -> None:
        args: list[Entity | Position] = []

        if self.entity is not None:
            args.append(self.entity)

        if self.position is not None:
            args.append(self.position)

        with self:
            self._func(*args)
