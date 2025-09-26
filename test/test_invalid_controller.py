from unittest import TestCase
from Url_Shortener.src.app import app
from Url_Shortener.src.config.config import url_collection


class TestInvalidFlaskRoutes(TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        url_collection.delete_many({})

    def test_shorten_empty_url(self):
        response = self.client.post("/shorten", json={"long": ""})
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("error", data)

    def test_shorten_none_url(self):
        response = self.client.post("/shorten", json={"long": None})
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("error", data)

    def test_shorten_invalid_format_url(self):
        invalid_urls = ["text", "htp://text", "://nothing", "www.read"]
        for url in invalid_urls:
            response = self.client.post("/shorten", json={"long": url})
            self.assertEqual(response.status_code, 400)
            data = response.get_json()
            self.assertIn("error", data)
