import unittest
import asyncio
from asyncio import coroutine
from aiourlshortener import Shortener

class TestGoogleShortener(unittest.TestCase):

    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)
        self.shortener = Shortener('Google', api_key='<api_key_here>')
        self.url = 'https://github.com/blikenoother/aiourlshortener'
        self.short_url = None

    def test_short_expand(self):
        @coroutine
        def short():
            self.short_url = yield from self.shortener.short(self.url)
            self.assertEqual(self.short_url, 'https://goo.gl/DPlXqT')
        self.loop.run_until_complete(short())

        @coroutine
        def expand():
            long_url = yield from self.shortener.expand(self.short_url)
            self.assertEqual(self.url, long_url)
        self.loop.run_until_complete(expand())


if __name__ == '__main__':
    unittest.main()

