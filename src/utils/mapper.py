from models.url import ShortenedUrlInfo

def map_to_url(document: dict) -> ShortenedUrlInfo:
    return ShortenedUrlInfo(**document)