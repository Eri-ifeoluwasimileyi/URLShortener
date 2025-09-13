from flask import Blueprint, request, redirect, jsonify
from Url_Shortener.src.services.url_service import URLService
from Url_Shortener.src.exceptions.errors import URLNotFoundError

urls = Blueprint("urls", __name__)

@urls.route("/shorten", methods=["POST"])
def shorten():
#endpoint to create a short URL from a long URL
    data = request.get_json()

    if not data or 'long' not in data:
        return jsonify({'error': "Missing long URL in the request"}), 400

    long_url = data.get("long")

    try:
        short_key = URLService.create_short_url(long_url)

        response = {
            'original_url': long_url,
            'short_url': short_key,
            'shortened_url': f'{request.url_root}{short_key}'
        }

        return jsonify(response), 201
    except URLNotFoundError:
        return jsonify({'error': "URL not found"}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@urls.route("/<short_url>")
#endpoint 2 redirects users from short url back to original url
def redirect_url(short_url):
    try:
        #find the original url that matches the short link
        long_url = URLService.get_long_url(short_url)

        #send the user to the original website by redirecting their browser
        return redirect(long_url)
    except URLNotFoundError as e:
        return jsonify({"error": str(e)}), 404

