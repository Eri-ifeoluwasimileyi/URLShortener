from database.url_repository import URLRepository
from database.users_repository import Users
from exceptions.url_exceptions import URLNotFoundError
from exceptions.user_exceptions import UserNotFoundError
from models.url import ShortenedUrlInfo, ShortenedURLRequest
from utils.shortener import generate_short_url


class URLService:
    def __init__(self, urls: URLRepository, users: Users):
        self.urls = urls
        self.users = users

    def create_short_url(self, request: ShortenedURLRequest) -> dict:
        user_data = self.users.get_user_by_id(request.user_id)
        if user_data is None:
            raise UserNotFoundError('User not found', 404)

        short_url = generate_short_url()
        # make unique url
        while self.urls.find_by_short_url(short_url):
            short_url = generate_short_url()

        url_info = ShortenedUrlInfo(
            user_id=request.user_id, short_url=short_url,
            long_url=request.long_url.encoded_string(),
            expires_in=request.expires_in if request.expires_in else None,
        )
        return self.urls.save(url=url_info)


    def get_long_url(self, short_url: str):
        url_data = self.urls.find_by_short_url(short_url)
        if not url_data:
            raise URLNotFoundError("URL not found")

        self.urls.update_clicks(short_url)
        return url_data['long_url']


    def find_url_info(self, short_url: str) -> dict:
        url_info = self.urls.find_by_short_url(short_url)
        if not url_info:
            raise URLNotFoundError("URL not found")
        return url_info


    def get_user_urls(self, user_id: str):
        urls_data = self.urls.find_by_user(user_id)
        if not urls_data:
            raise URLNotFoundError("No Urls Found")
        return urls_data

