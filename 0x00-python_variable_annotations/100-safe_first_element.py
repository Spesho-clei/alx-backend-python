#!/usr/bin/env python3

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Takes a sequence lst and returns its first element if it exists, otherwise returns None.
    """
    if lst:
        return lst[0]
    else:
        return None
