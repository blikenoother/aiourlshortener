import aiourlshortener.shorteners.google

import tests.test_shorteners
from tests.utils import URLpair
from tests.credentials import CREDENTIALS


class GoogleTester(tests.test_shorteners.ShortenerTester):
    provider = 'Google'
    cls = aiourlshortener.shorteners.google.Google
    url_pair = URLpair(shorted='https://goo.gl/YWbCqB',
                       expanded='https://github.com/')
    kwargs = dict(api_key=CREDENTIALS.Google)
