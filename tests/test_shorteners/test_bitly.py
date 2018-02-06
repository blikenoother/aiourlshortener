import aiourlshortener.shorteners.bitly

import tests.test_shorteners
from tests.utils import URLpair
from tests.credentials import CREDENTIALS, check_for_credentials


@check_for_credentials(
    provider='Bitly',
    credentials_hint=(
        'Navigate to '
        'https://bitly.com/a/oauth_apps'
        ' -> "Generic Access Token"'
    )
)
class BitlyTester(tests.test_shorteners.ShortenerTester):
    provider = 'Bitly'
    cls = aiourlshortener.shorteners.bitly.Bitly
    url_pair = URLpair(shorted='http://bit.ly/2ElUnG9',
                       expanded='https://github.com/')
    kwargs = dict(access_token=CREDENTIALS.Bitly)
