from abc import ABC, abstractmethod


from src.models.url import ShortenedUrlInfo


class UrlInterface(ABC):

    @abstractmethod
    def save(self, url: ShortenedUrlInfo):
        pass

    @abstractmethod
    def find_by_short_url(self, short_url:str):
        pass

    @abstractmethod
    def update_clicks(self, short_url: str):
        pass

    @abstractmethod
    def find_by_user(self, user_id: str):
        pass