__all__ = (
    'CREDENTIALS',
    'check_for_credentials',
)

import logging
import os
import unittest
from collections import namedtuple

import aiourlshortener.shorteners


_ENV_PREFIX = 'AIOURLSHORTENER_'
_CREDENTIALS_TEMPLATE = (
    'Credentials for "{provider}" are missing!\n\t{hint}\nAdd them into '
    'your environment with:\n\t`$ export {prefix}{provider_upper}="<TOKEN>"`'
)
_PROVIDERS = aiourlshortener.shorteners._shorten_class.keys()
_CREDENTIALS = {}
_MISSING = object()
logger = logging.getLogger(__name__)

for provider in _PROVIDERS:
    provider_upper = provider.upper()
    try:
        _CREDENTIALS[provider] = os.environ[_ENV_PREFIX + provider_upper]
    except KeyError:
        _CREDENTIALS[provider] = _MISSING


Credentials = namedtuple(
    'Credentials',
    _CREDENTIALS.keys()
)
CREDENTIALS = Credentials(**_CREDENTIALS)


def check_for_credentials(provider, credentials_hint):
    if _CREDENTIALS[provider] is _MISSING:
        return unittest.skip(
            _CREDENTIALS_TEMPLATE.format(
                provider=provider, provider_upper=provider.upper(),
                prefix=_ENV_PREFIX, hint=credentials_hint,
            )
        )
    else:
        def do_not_touch(cls):
            return cls

        return do_not_touch
