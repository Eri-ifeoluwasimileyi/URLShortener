import validators


def validate_url_data(data: dict):
    if not data or 'long' not in data:
        return False
    if validators.url(data.get('long')):
        return True
    return False

