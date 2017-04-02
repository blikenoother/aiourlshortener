aiourlshortener
===============

aiourlshortener is a `asyncio <https://pypi.python.org/pypi/asyncio>`__
python3 compatible library for URL shorting using
`Googl <https://goo.gl/>`__, `Bitly <https://bitly.com/>`__ API

Installing
==========

::

    pip3 install aiourlshortener

Requirements
============

-  `asyncio <https://pypi.python.org/pypi/asyncio>`__ or Python 3.4+
-  `aiohttp <https://pypi.python.org/pypi/aiohttp>`__

Usage
=====

Create a Shortener instance passing the engine as an argument.

Goo.gl Shortener
----------------

``api_key`` required

.. code:: python

    import asyncio
    from asyncio import coroutine
    from aiourlshortener import Shortener

    @coroutine
    def main():
        shortener = Shortener('Google', api_key='API_KEY')
        url = 'https://github.com/blikenoother/aiourlshortener'
        # short
        short_url = yield from shortener.short(url)
        print('short url: {}'.format(short_url))
        # expand
        long_url = yield from shortener.expand(short_url)
        print('long url: {}'.format(long_url))

    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())

Bit.ly Shortener
----------------

``access_token`` required

.. code:: python

    import asyncio
    from asyncio import coroutine
    from aiourlshortener import Shortener

    @coroutine
    def main():
        shortener = Shortener('Bitly', access_token='ACCESS_TOKEN')
        url = 'https://github.com/blikenoother/aiourlshortener'
        # short
        short_url = yield from shortener.short(url)
        print('short url: {}'.format(short_url))
        # expand
        long_url = yield from shortener.expand(short_url)
        print('long url: {}'.format(long_url))

    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
