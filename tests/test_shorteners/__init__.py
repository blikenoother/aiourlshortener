__all__ = (
    'ShortenerTester',
)

import asyncio
import inspect
import unittest

import aiourlshortener.shorteners.base

import tests.utils


class ShortenerTester(unittest.TestCase):
    # < must be set by child >
    provider = None
    """str: the shortener provider name"""

    cls = None
    """aiourlshortener.shorteners.base.BaseShortener: a derived class"""

    url_pair = None
    """tests.utils.URLpair: shortened url and expanded url pair"""

    kwargs = None
    """mixed: the keyword arguments for an instance, including tokens"""

    # </ must be set by child >

    # < tests >

    def test_attributes(self):
        self.assertIsInstance(self.provider, str)
        assert issubclass(self.cls,
                          aiourlshortener.shorteners.base.BaseShortener)
        self.assertFalse(inspect.isabstract(self.cls))
        self.assertIsInstance(self.url_pair, tests.utils.URLpair)
        self.assertIsInstance(self.kwargs, dict)

    @tests.utils.with_new_loop
    def test_short(self):
        instance = self.cls(**self.kwargs)
        url = self.await(instance.short(self.url_pair.expanded))
        self.assertIsInstance(url, str)
        # the url differs per user, do not validate further

    @tests.utils.with_new_loop
    def test_expand(self):
        instance = self.cls(**self.kwargs)
        url = self.await(instance.expand(self.url_pair.shorted))
        self.assertEqual(url, self.url_pair.expanded)

    # </ tests >

    # < private interface >

    @staticmethod
    def await(coro_or_future):
        return asyncio.get_event_loop().run_until_complete(coro_or_future)

    # </ private interface >
