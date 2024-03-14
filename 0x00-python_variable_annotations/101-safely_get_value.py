#!/usr/bin/env python3

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Takes a dictionary dct, a key key, and an optional default value default.
    If key is in dct, returns dct[key], otherwise returns the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
