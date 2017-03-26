# aiourlshortener

aiourlshortener is a [asyncio](https://pypi.python.org/pypi/asyncio) python3 compatible library for URL shorting using [Googl](https://goo.gl/), [Bitly](https://bitly.com/) API

# Installing

clone repository and just follow this steps

```
git clone git@github.com:blikenoother/aiourlshortener.git
cd aiourlshortener
python3 setup.py install
```

Installing via pip3 package manager

```
pip3 install -e git+git@github.com:blikenoother/aiourlshortener.git#egg=aiourlshortener
```

# Usage

Create a Shortener instance passing the engine as an argument.

## Goo.gl Shortener

`api_key` required

```python
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

```

## Bit.ly Shortener

`access_token` required

```python
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
```