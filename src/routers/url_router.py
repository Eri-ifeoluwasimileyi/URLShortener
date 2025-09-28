from flask import Blueprint, request, jsonify, redirect
from flask_jwt_extended import jwt_required, get_jwt_identity
from configuration.injections import get_url_service
from exceptions.url_exceptions import URLNotFoundError, ExpiredURLError, MissingURLDataError
from models.url import ShortenedURLRequest

urls_bp = Blueprint('urls', __name__, url_prefix='/urls')

@urls_bp.route('/shorten', methods=['POST'])
@jwt_required()
def shorten_url():
    url_service = get_url_service()
    data = request.json
    if data is None:
        raise MissingURLDataError("Missing URL")

    user_id = get_jwt_identity()
    shortened_url_request = ShortenedURLRequest(user_id=user_id, **data)
    saved_url_data = url_service.create_short_url(request=shortened_url_request)

    return jsonify({
        'shortened_url': f'{request.url_root}{saved_url_data["short_url"]}',
        **saved_url_data
    }), 201


@urls_bp.route("/<short_url>")
def redirect_url(short_url):
    url_service = get_url_service()
    try:
        #find the original url that matches the short link
        long_url = url_service.get_long_url(short_url)
        return redirect(long_url)
    except URLNotFoundError as e:
        return jsonify({"error": str(e)}), 404


@urls_bp.route('/<short_url>/stats', methods=['GET'])
@jwt_required()
def get_url_stats(short_url):
    url_service = get_url_service()
    url_data = url_service.find_url_info(short_url)
    return jsonify(url_data), 200


@urls_bp.route('/urls', methods=['GET'])
@jwt_required()
def get_user_urls():
    user_id = get_jwt_identity()
    url_service = get_url_service()
    urls_data = url_service.get_user_urls(user_id)
    return jsonify(urls_data), 200
