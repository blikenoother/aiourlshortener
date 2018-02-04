import inspect
from asyncio import coroutine
from importlib.machinery import SourceFileLoader
import os

from .base import BaseShortener
from ..exceptions import UnknownAioUrlShortenerError
from ..utils import url_validator

_shorten_class = {}
_path = os.path.dirname(os.path.realpath(__file__))
for file in os.listdir(_path):
    if file.startswith('__') or file == 'base.py':
        continue
    _shorten = SourceFileLoader('aiourlshortener.shorteners.', '{}/{}'.format(_path, file)).load_module()
    for attr in dir(_shorten):
        tmp_cls = getattr(_shorten, attr)
        if attr != 'BaseShortener' and inspect.isclass(tmp_cls) and issubclass(tmp_cls, BaseShortener) and not inspect.isabstract(tmp_cls):
            _shorten_class[attr] = tmp_cls

__all__ = ['Shorteners', 'Shortener']


class Shorteners(object):
    GOOGLE = 'Google'
    BITLY = 'Bitly'


class Shortener(object):
    """
    Factory class for all Shorteners
    """

    def __init__(self, engine, **kwargs):
        self.kwargs = kwargs
        self.shorten = None
        self.expanded = None

        if inspect.isclass(engine) and issubclass(engine, BaseShortener) and not inspect.isabstract(engine):
            self.engine = engine.__name__
            self._class = engine
        elif engine in _shorten_class:
            self.engine = engine
            self._class = _shorten_class[self.engine]
        else:
            raise UnknownAioUrlShortenerError('Please enter a valid shortener. {} class does not exist'.
                                              format(engine))

        for key, item in list(kwargs.items()):
            setattr(self, key, item)

    @property
    def api_url(self):
        return self._class.api_url

    @coroutine
    def short(self, url: str) -> str:
        """
        get short url for given long url

        :param str url: valid url string

        :yield: short url
        :rtype: str
        :raises: ValueError, ShorteningError
        """
        url_validator(url)
        self.expanded = url

        instance = self._class(**self.kwargs)
        try:
            self.shorten = yield from instance.short(url)
        finally:
            yield from instance.close()

        return self.shorten

    @coroutine
    def expand(self, url: str) -> str:
        """
        expand given short url to long url

        :param str url: valid url string

        :yield: long url
        :rtype: str
        :raises: ValueError, ExpandingError
        """
        url_validator(url)
        self.shorten = url

        instance = self._class(**self.kwargs)
        try:
            self.expanded = yield from instance.expand(url)
        finally:
            yield from instance.close()

        return self.expanded
