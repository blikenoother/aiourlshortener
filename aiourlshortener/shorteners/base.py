from abc import abstractmethod
import aiohttp
from asyncio import coroutine


class BaseShortener(object):
    """
    Base class for all Shorteners
    """
    api_url = None
    _session = None

    def __init__(self, **kwargs):
        self._session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(use_dns_cache=True))
        self.kwargs = kwargs

    @coroutine
    def _get(self, url: str, params=None, headers=None):
        with aiohttp.Timeout(self.kwargs['timeout']):
            response = yield from self._session.get(url, params=params, headers=headers)
            return response

    @coroutine
    def _post(self, url: str, data=None, params=None, headers=None):
        with aiohttp.Timeout(self.kwargs['timeout']):
            response = yield from self._session.post(url, data=data, params=params, headers=headers)
            return response

    @abstractmethod
    def short(self, url: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def expand(self, url: str) -> str:
        raise NotImplementedError

    @coroutine
    def close(self):
        if self._session is not None:
            yield from self._session.close()

    def __del__(self):
        if self._session is not None and not self._session.closed:
            self._session.close()

    @classmethod
    def __subclasshook__(cls, c):
        if cls is BaseShortener:
            if all(hasattr(c, name) for name in ('short', 'expand')):
                return True
        return NotImplemented
