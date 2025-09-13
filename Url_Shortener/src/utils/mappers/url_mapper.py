from Url_Shortener.src.models.shortenedURL import ShortenedURL


#convert a dictionary from database into an object,returns None if short/long is missing
def map_to_url(document: dict) -> ShortenedURL | None:
    if not document:
        return None

    short_url = document.get('short')
    long_url = document.get('long')

    #create and return the ShortenedURL object
    return ShortenedURL(short=short_url, long=long_url)
