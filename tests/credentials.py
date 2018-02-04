__all__ = (
    'CREDENTIALS',
)

import logging
import os
from collections import namedtuple

import aiourlshortener.shorteners


_ENV_PREFIX = 'AIOURLSHORTENER_'
_PROVIDERS = aiourlshortener.shorteners._shorten_class.keys()
_CREDENTIALS = {}
logger = logging.getLogger(__name__)

for provider in _PROVIDERS:
    provider_upper = provider.upper()
    try:
        _CREDENTIALS[provider] = os.environ[_ENV_PREFIX + provider_upper]
    except KeyError:
        pass
    else:
        _CREDENTIALS[provider_upper] = _CREDENTIALS[provider]


Credentials = namedtuple(
    'Credentials',
    _CREDENTIALS.keys()
)
CREDENTIALS = Credentials(**_CREDENTIALS)
