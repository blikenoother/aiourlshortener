import asyncio
from abc import abstractmethod
import aiohttp
from asyncio import coroutine

from ..exceptions import FetchError


class BaseShortener(object):
    """
    Base class for all Shorteners
    """
    api_url = None

    def __init__(self, **kwargs):
        self._session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(use_dns_cache=True))
        self.kwargs = kwargs

    @coroutine
    def _get(self, url: str, params=None, headers=None):
        response = yield from self._fetch('GET', url, params=params, headers=headers)
        return response

    @coroutine
    def _post(self, url: str, data=None, params=None, headers=None):
        response = yield from self._fetch('POST', url, data=data, params=params, headers=headers)
        return response

    @coroutine
    def _fetch(self, method: str, url: str, data=None, params=None, headers=None):
        try:
            with aiohttp.Timeout(self.kwargs['timeout']):
                response = yield from self._session.request(method, url, data=data, params=params, headers=headers)
                response.raise_for_status()
        except (aiohttp.ClientError, asyncio.TimeoutError):
            raise FetchError()
        else:
            return response

    @abstractmethod
    def short(self, url: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def expand(self, url: str) -> str:
        raise NotImplementedError

    @coroutine
    def close(self):
        try:
            yield from self._session.close()
        except TypeError:
            pass

    @classmethod
    def __subclasshook__(cls, c):
        if cls is BaseShortener:
            if all(hasattr(c, name) for name in ('short', 'expand')):
                return True
        return NotImplemented
