class URLNotFoundError(Exception):
        def __init__(self, message):
                super().__init__(message)


class ShortURLCollisionError(Exception):
        def __init__(self, message):
                super().__init__(message)

