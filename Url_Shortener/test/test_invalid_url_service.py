from unittest import TestCase
from Url_Shortener.src.services.url_service import URLService
from Url_Shortener.src.config.config import url_collection
from Url_Shortener.src.exceptions.errors import URLNotFoundError


class TestInvalidURLService(TestCase):

    def setUp(self):
        url_collection.delete_many({})

    def test_empty_string_url(self):
        with self.assertRaises(ValueError):
            URLService.create_short_url("")

    def test_none_url(self):
        with self.assertRaises(ValueError):
            URLService.create_short_url(None)

    def test_invalid_format_url(self):
        invalid_urls = ["justtext", "htp://wrong", "://missing", "www.example"]
        for url in invalid_urls:
            with self.assertRaises(ValueError):
                URLService.create_short_url(url)
