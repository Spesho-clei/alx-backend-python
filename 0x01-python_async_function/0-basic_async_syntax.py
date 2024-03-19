#!/usr/bin/env python3
""" task 0 module """

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: Random delay.
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
