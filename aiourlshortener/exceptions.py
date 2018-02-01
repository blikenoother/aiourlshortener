class UnknownAioUrlShortenerError(Exception):
    pass


class FetchError(Exception):
    """A error occurred while fetching a remote resource"""


class ShorteningError(Exception):
    pass


class ExpandingError(Exception):
    pass
