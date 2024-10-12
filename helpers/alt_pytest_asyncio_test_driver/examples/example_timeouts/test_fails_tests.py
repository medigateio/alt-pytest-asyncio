import asyncio

import pytest

pytestmark = pytest.mark.async_timeout(0.01)


async def test_takes_closest_pytestmark():
    await asyncio.sleep(0.03)


@pytest.mark.async_timeout(0.04)
async def test_takes_pytestmark_on_function():
    await asyncio.sleep(0.03)


@pytest.mark.async_timeout(0.02)
async def test_takes_pytestmark_on_function2():
    await asyncio.sleep(0.03)
