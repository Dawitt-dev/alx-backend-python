#!/usr/bin/env python3
"""Function that returns an asyncio.Task"""
import asyncio
from importlib import import_module

# Dynamically import the wait_random function
basic_async_syntax = import_module('0-basic_async_syntax')
wait_random = basic_async_syntax.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for wait_random(max_delay).

    Parameters:
    max_delay (int): Maximum delay for wait_random.

    Returns:
    asyncio.Task: The created asyncio.Task.
    """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == "__main__":
    # Example usage
    task = task_wait_random(5)
    print(task)
