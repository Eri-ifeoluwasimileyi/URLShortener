from Url_Shortener.src.config.config import url_collection
from Url_Shortener.src.models.shortenedURL import ShortenedURL
class URLRepository:

    @staticmethod
    def save(url: ShortenedURL):
        url_collection.insert_one(
            {"short": url.short,
            "long": url.long
             })

    @staticmethod
    def find_by_short(short: str):
        return url_collection.find_one({"short": short})
