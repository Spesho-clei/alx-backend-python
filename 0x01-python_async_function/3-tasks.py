#!/usr/bin/env python3

""" task 3 module """

import asyncio
from typing import Coroutine

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for wait_random with the specified max_delay.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: Task object representing the execution of wait_random.
    """
    coroutine = wait_random(max_delay)
    task = asyncio.create_task(coroutine)
    return task
