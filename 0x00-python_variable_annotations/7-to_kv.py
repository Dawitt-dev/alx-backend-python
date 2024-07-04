#!/usr/bin/env python3
"""A type-annotated function to_kv which takes a string
k and an int OR float v as arguments and returns a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string k and an int or float v
    and returns a tuple where the first element is the string k
    and the second element is the square of the int/float v.
    """
    return (k, float(v ** 2))
