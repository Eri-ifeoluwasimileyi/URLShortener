from src.models.shortenedURL import ShortenedURL


def map_to_url(document: dict) -> ShortenedURL | None:
    if not document:
        return None

    short_url = document.get('short')
    long_url = document.get('long')

    return ShortenedURL(short=short_url, long=long_url)
