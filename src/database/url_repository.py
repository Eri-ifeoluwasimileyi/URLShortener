from datetime import datetime
from typing import Optional
from pymongo.synchronous.database import Database


class URLRepository(UrlInterface):
    def __init__(self, db: Database):
        self.db = db
        self.urls_collection = self.db.get_collection("urls")
        self.urls_collection.create_index([('expires_in', 1)], expireAfterSeconds=0)

    def save(self, url: ShortenedUrlInfo):
        url_data = url.model_dump(exclude_none=True)
        self.urls_collection.insert_one(url_data.copy())
        return url_data

    def find_by_short_url(self, short_url: str) -> Optional[dict]:
        document: dict = self.urls_collection.find_one({'short_url': short_url})
        if not document:
            return None
        document.pop("_id")
        return document

    def update_clicks(self, short_url: str) -> None:
        self.urls_collection.update_one(
            {'short_url': short_url},
            {'$inc': {'clicks_count': 1},
             '$set': {'last_accessed': datetime.now()},
             }
        )

    def find_by_user(self, user_id: str) -> list[dict]:
        documents = self.urls_collection.find({'user_id': user_id}).to_list()
        for document in documents:
            document.pop("_id")
        return documents
