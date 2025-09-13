from Url_Shortener.src.utils.mappers.url_mapper import map_to_url
from Url_Shortener.src.utils.url_shortener import generate_short_url
from Url_Shortener.src.repository.url_repository import URLRepository
from Url_Shortener.src.exceptions.errors import URLNotFoundError
from Url_Shortener.src.models.shortenedURL import ShortenedURL

class URLService:
    @staticmethod
    def create_short_url(long_url: str) -> str:
        short_url = generate_short_url()

        # makes a unique url
        while URLRepository.find_by_short(short_url):
            short_url = generate_short_url()

        url = ShortenedURL(short=short_url, long=long_url)
        URLRepository.save(url)
        return short_url

    @staticmethod
    def get_long_url(short_url: str) -> str:
        document = URLRepository.find_by_short(short_url)

        if not document:
            raise URLNotFoundError("URL not found")

        url_obj = map_to_url(document)
        return url_obj.long


