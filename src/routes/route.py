from flask import Blueprint, request, redirect, jsonify
from src.services.url_service import URLService
from src.exceptions.errors import URLNotFoundError
from src.utils.validators import validate_url_data

urls = Blueprint("urls", __name__)

@urls.route("/shorten", methods=["POST"])
def shorten():
    data = request.get_json()
    if not validate_url_data(data):
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
def redirect_url(short_url):
    try:
        #find the original url that matches the short link
        long_url = URLService.get_long_url(short_url)

        return redirect(long_url)
    except URLNotFoundError as e:
        return jsonify({"error": str(e)}), 404

