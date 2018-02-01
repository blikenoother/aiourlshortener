"""
Google Shortener Implementation
Needs API_KEY
"""
import json
from asyncio import coroutine

from .base import BaseShortener
from ..exceptions import ShorteningError, ExpandingError


class Google(BaseShortener):
    api_url = 'https://www.googleapis.com/urlshortener/v1/url'

    _headers = {'content-type': 'application/json'}

    def __init__(self, **kwargs):
        if not kwargs.get('api_key', False):
            raise TypeError('api_key missing from kwargs')
        self.api_key = kwargs['api_key']
        super(Google, self).__init__(**kwargs)

    @coroutine
    def short(self, url: str) -> str:
        data = {'longUrl': url}
        params = {'key': self.api_key}
        response = yield from self._post(self.api_url, data=json.dumps(data), params=params, headers=self._headers)
        response = yield from response.json()
        if 'id' in response:
            return response['id']
        raise ShorteningError('There was an error shortening this url: {}'.format(response))

    @coroutine
    def expand(self, url: str) -> str:
        params = {'key': self.api_key, 'shortUrl': url}
        response = yield from self._get(self.api_url, params=params, headers=self._headers)
        response = yield from response.json()
        if 'longUrl' in response:
            return response['longUrl']
        raise ExpandingError('There was an error expanding this url: {}'.format(response))
