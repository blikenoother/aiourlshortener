from abc import abstractmethod, ABC
import asyncio
import aiohttp
from asyncio import coroutine

from ..exceptions import FetchError


DEFAULT_TIMEOUT = 10


class BaseShortener(ABC):
    """
    Base class for all Shorteners
    """
    api_url = None
    _session = None

    def __init__(self, timeout=DEFAULT_TIMEOUT):
        self._session = aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(use_dns_cache=True),
            conn_timeout=timeout,
        )

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
