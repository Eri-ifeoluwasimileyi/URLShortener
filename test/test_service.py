from unittest import TestCase
from Url_Shortener.src.services.url_service import URLService
from Url_Shortener.src.config.config import url_collection
from Url_Shortener.src.exceptions.errors import URLNotFoundError


class TestURLService(TestCase):

    def setUp(self):
        # Clean DB before each test
        url_collection.delete_many({})

    def test_create_short_url_and_retrieve(self):
        long_url = "https://testing.com"
        short_url = URLService.create_short_url(long_url)
        self.assertIsInstance(short_url, str)
        self.assertTrue(len(short_url) > 0)
        retrieved = URLService.get_long_url(short_url)
        self.assertEqual(retrieved, long_url)

    def test_get_long_url_not_found(self):
        with self.assertRaises(URLNotFoundError):
            URLService.get_long_url("invalid123")

    def test_multiple_url_shortening(self):
        urls = ["https://testing.com/1", "https://testing.com/2", "https://testing.com/3"]
        shorts = []
        for url in urls:
            short = URLService.create_short_url(url)
            shorts.append(short)
            self.assertIsInstance(short, str)
            self.assertTrue(len(short) > 0)
        for i, short in enumerate(shorts):
            retrieved = URLService.get_long_url(short)
            self.assertEqual(retrieved, urls[i])

    def test_same_url_returns_different_short_urls(self):
        url = "https://testing.com/thesameurl"
        short1 = URLService.create_short_url(url)
        short2 = URLService.create_short_url(url)
        self.assertNotEqual(short1, short2)

    def test_invalid_short_url_returns_error(self):
        invalid_shorts = ["abc123", "", None]
        for short in invalid_shorts:
            with self.assertRaises(URLNotFoundError):
                URLService.get_long_url(short)


    def test_long_url(self):
        long_url = "https://testing.com/" + "a" * 5000
        short = URLService.create_short_url(long_url)
        retrieved = URLService.get_long_url(short)
        self.assertEqual(retrieved, long_url)

    def test_url_with_query_params(self):
        long_url = "https://testing.com/search?q=openai&lang=en"
        short = URLService.create_short_url(long_url)
        retrieved = URLService.get_long_url(short)
        self.assertEqual(retrieved, long_url)

    def test_url_with_special_characters(self):
        long_url = "https://testing.com/path/!@#$%^&*()_+-=[]{}|;':,.<>?/~`"
        short = URLService.create_short_url(long_url)
        retrieved = URLService.get_long_url(short)
        self.assertEqual(retrieved, long_url)
