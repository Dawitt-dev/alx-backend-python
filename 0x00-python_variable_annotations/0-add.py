#!/usr/bin/env python3
"""a type-annotated function add"""


def add(a: float, b: float) -> float:
    """that takes a float a and a float b as
    arguments and returns their sum as a float
    """
    return a + b


if __name__ == "__main__":
    add()
