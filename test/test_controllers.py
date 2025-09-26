from unittest import TestCase
from Url_Shortener.src.app import app
from Url_Shortener.src.config.config import url_collection


class TestFlaskRoutes(TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        url_collection.delete_many({})

    def test_shorten_and_redirect(self):
        response = self.client.post("/shorten", json={"long": "https://testing.com"})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("shortened_url", data)
        short_url = data["shortened_url"].split("/")[-1]
        redirect_response = self.client.get(f"/{short_url}", follow_redirects=False)
        self.assertEqual(redirect_response.status_code, 302)
        self.assertEqual(redirect_response.location, "https://testing.com")

    def test_redirect_not_found(self):
        response = self.client.get("/nonexistent123")
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data.get("error"), "URL not found")


    def test_shorten_long_url(self):
        long_url = "https://testing.com/" + "a" * 5000
        response = self.client.post("/shorten", json={"long": long_url})
        self.assertEqual(response.status_code, 200)
        short_url = response.get_json()["shortened_url"].split("/")[-1]
        redirect_response = self.client.get(f"/{short_url}", follow_redirects=False)
        self.assertEqual(redirect_response.location, long_url)

    def test_shorten_url_with_query_params(self):
        long_url = "https://testing.com/search?q=openai&lang=en"
        response = self.client.post("/shorten", json={"long": long_url})
        self.assertEqual(response.status_code, 200)
        short_url = response.get_json()["shortened_url"].split("/")[-1]
        redirect_response = self.client.get(f"/{short_url}", follow_redirects=False)
        self.assertEqual(redirect_response.location, long_url)
