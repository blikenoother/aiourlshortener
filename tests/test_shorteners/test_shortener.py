import inspect

import pytest

import aiourlshortener.exceptions
import aiourlshortener.shorteners
import aiourlshortener.shorteners.base


class DemoShortenerHalf(aiourlshortener.shorteners.base.BaseShortener):
    def expand(self, url):
        return ''


class DemoShortener(DemoShortenerHalf):
    def short(self, url):
        return ''


# inject the test class
aiourlshortener.shorteners._shorten_class['DemoShortener'] = DemoShortener


def test_demo_classes():
    assert inspect.isabstract(DemoShortenerHalf)
    assert not inspect.isabstract(DemoShortener)


def test_shortener_by_class():
    with pytest.raises(aiourlshortener.exceptions.UnknownAioUrlShortenerError):
        shortener = aiourlshortener.Shortener(DemoShortenerHalf)

    shortener = aiourlshortener.Shortener(DemoShortener)
    assert shortener._class is DemoShortener


def test_shortener_by_name():
    with pytest.raises(aiourlshortener.exceptions.UnknownAioUrlShortenerError):
        shortener = aiourlshortener.Shortener('RandomName')

    shortener = aiourlshortener.Shortener('DemoShortener')
    assert shortener._class is DemoShortener
