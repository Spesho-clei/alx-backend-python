#!/usr/bin/env python3

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences lst and returns a list of tuples.
    Each tuple contains an element of lst and its length.
    """
    return [(i, len(i)) for i in lst]
