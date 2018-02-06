import aiourlshortener.shorteners.google

import tests.test_shorteners
from tests.utils import URLpair
from tests.credentials import CREDENTIALS, check_for_credentials


@check_for_credentials(
    provider='Google',
    credentials_hint=(
        'Navigate to '
        'https://developers.google.com/url-shortener/v1/getting_started#APIKey'
        ' -> "GET A KEY"'
    )
)
class GoogleTester(tests.test_shorteners.ShortenerTester):
    provider = 'Google'
    cls = aiourlshortener.shorteners.google.Google
    url_pair = URLpair(shorted='https://goo.gl/YWbCqB',
                       expanded='https://github.com/')
    kwargs = dict(api_key=CREDENTIALS.Google)
