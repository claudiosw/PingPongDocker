class HttpRequestError(Exception):

    def __init__(self, message: str, status_code: int) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'HttpRequestError'
        self.status_code = status_code
