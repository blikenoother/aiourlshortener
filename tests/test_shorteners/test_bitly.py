import aiourlshortener.shorteners.bitly

import tests.test_shorteners
from tests.utils import URLpair
from tests.credentials import CREDENTIALS


class BitlyTester(tests.test_shorteners.ShortenerTester):
    provider = 'Bitly'
    cls = aiourlshortener.shorteners.bitly.Bitly
    url_pair = URLpair(shorted='http://bit.ly/2ElUnG9',
                       expanded='https://github.com/')
    kwargs = dict(access_token=CREDENTIALS.Bitly)
