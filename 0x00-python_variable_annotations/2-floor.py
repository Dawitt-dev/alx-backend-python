#!/usr/bin/env python3
"""a type-annotated function floor which takes a float
n and returns the floor of the float.
"""
import math


def floor(n: float) -> int:
    """a type-annotated function floor which takes
    a float n as argument and returns the floor of the float.
    """
    return math.floor(n)


if __name__ == "__main__":
    floor()
