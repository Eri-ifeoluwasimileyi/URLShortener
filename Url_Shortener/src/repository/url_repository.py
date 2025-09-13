from Url_Shortener.src.config.config import url_collection
from Url_Shortener.src.models.shortenedURL import ShortenedURL
# helper class to interact with the database, it saves urls and find them by their short code
class URLRepository:

    @staticmethod #we don't need to create an instance of the class
    def save(url: ShortenedURL):
        url_collection.insert_one(
            {"short": url.short,
            "long": url.long
             })

    @staticmethod
    def find_by_short(short: str):
        return url_collection.find_one({"short": short})
