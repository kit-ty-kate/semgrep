from itertools import chain
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar, Union

C = TypeVar("C")

def _indent(
    text: str, margin: str, newline: str = ..., key: Type[bool] = ...
) -> str: ...
def copy_function(orig: Callable, copy_dict: bool = ...) -> Callable: ...
def mro_items(type_obj: Type[C]) -> chain: ...
def wraps(
    func: Union[classmethod, Callable],
    injected: Optional[Union[str, List[str]]] = ...,
    **kw: Any,
) -> Callable: ...

class CachedInstancePartial:
    def __get__(self, obj: C, obj_type: Type[C]) -> Callable: ...

class FunctionBuilder:
    def __init__(self, name: str, **kw: Any) -> None: ...
    @classmethod
    def _argspec_to_dict(cls, f: Callable) -> Dict[str, Any]: ...
    def _compile(self, src: str, execdict: Dict[Any, Any]) -> Dict[Any, Any]: ...
    @classmethod
    def from_func(cls, func: Callable) -> FunctionBuilder: ...
    def get_defaults_dict(self) -> Dict[str, str]: ...
    def get_func(
        self,
        execdict: Optional[Dict[str, Callable]] = ...,
        add_source: bool = ...,
        with_dict: bool = ...,
    ) -> Callable: ...
    def get_invocation_str(self) -> str: ...
    def get_sig_str(self) -> str: ...
    def remove_arg(self, arg_name: str) -> None: ...

class InstancePartial:
    def __get__(self, obj: C, obj_type: Type[C]) -> Callable: ...