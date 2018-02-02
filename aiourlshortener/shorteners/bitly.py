"""
Bitly Shortener Implementation
Needs ACCESS_TOKEN
"""
from asyncio import coroutine

import aiohttp

from .base import BaseShortener
from ..exceptions import ShorteningError, ExpandingError, FetchError


class Bitly(BaseShortener):
    api_url = 'https://api-ssl.bitly.com/v3'

    _short_url = '{}/shorten'.format(api_url)
    _expand_url = '{}/link/info'.format(api_url)

    def __init__(self, access_token, **kwargs):
        self.access_token = access_token
        super(Bitly, self).__init__(**kwargs)

    @coroutine
    def short(self, url: str) -> str:
        params = {'access_token': self.access_token, 'longUrl': url, 'format': 'json'}
        response = {}
        try:
            response = yield from self._get(self._short_url, params=params)
            response = yield from response.json()
        except (aiohttp.ClientError, FetchError) as err:
            raise ShorteningError('There was an error shortening the url "{}": {}'.format(url, repr(err)))

        if 'data' in response and isinstance(response['data'], dict) and 'url' in response['data']:
            return response['data']['url']

        raise ShorteningError('Detected an api change for Bitly')

    @coroutine
    def expand(self, url: str) -> str:
        params = {'access_token': self.access_token, 'link': url, 'format': 'json'}
        response = {}
        try:
            response = yield from self._get(self._expand_url, params=params)
            response = yield from response.json()
        except (aiohttp.ClientError, FetchError) as err:
            raise ExpandingError('There was an error expanding the url "{}": {}'.format(url, repr(err)))

        if 'data' in response and isinstance(response['data'], dict) and 'original_url' in response['data']:
            return response['data']['original_url']

        raise ExpandingError('Detected an api change for Bitly')
