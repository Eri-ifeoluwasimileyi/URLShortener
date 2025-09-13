class URLNotFoundError(Exception):
        """Raised when a short URL is not found in the database"""

class ShortURLCollisionError(Exception):
        """Raised when a generated short URL already exists"""
