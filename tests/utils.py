__all__ = (
    'URLpair',
    'with_new_loop',
)

import asyncio
import collections
import logging

URLpair = collections.namedtuple('URLpair', ['shorted', 'expanded'])


logger = logging.getLogger(__name__)


def with_new_loop(func):
    """function decorator for creating a clean asyncio event loop per call"""
    def wrapper(*args, **kwargs):
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        mixed = None
        try:
            mixed = func(*args, **kwargs)
        finally:
            try:
                new_loop.run_until_complete(asyncio.sleep(0.1))
                new_loop.close()
            except RuntimeError:
                logger.info('EventLoop still running: %r', new_loop)

        return mixed

    return wrapper
