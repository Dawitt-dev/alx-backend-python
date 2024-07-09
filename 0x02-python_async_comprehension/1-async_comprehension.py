#!/usr/bin/env python3
"""Async Comprehension Example"""
import asyncio
from typing import List
from importlib import import_module


# Import async_generator from the previous task
async_generator = import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async
    comprehension over async_generator.

    Returns:
    List[float]: A list of 10 random numbers.
    """
    return [i async for i in async_generator()][:10]


if __name__ == "__main__":
    async def main() -> None:
        print(await async_comprehension())

    asyncio.run(main())
