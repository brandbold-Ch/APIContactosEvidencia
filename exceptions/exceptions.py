from typing import Optional


class BaseHTTPException(Exception):
    def __init__(
        self,
        message: str,
        http_code: int,
        error_code: Optional[str] = None,
        data: Optional[dict] = None
    ):
        self.message = message
        self.http_code = http_code
        self.error_code = error_code or f"HTTP_{http_code}"
        self.data = data or {}

    def to_dict(self) -> dict:
        return {
            "message": self.message,
            "code": self.http_code,
            "error": self.error_code,
            "data": self.data
        }

    def __str__(self):
        return f"[{self.http_code}] {self.error_code}: {self.message}"


class OK(BaseHTTPException):
    def __init__(self, message="Success", data=None):
        super().__init__(message, http_code=200, error_code="OK", data=data)


class Created(BaseHTTPException):
    def __init__(self, message="Created", data=None):
        super().__init__(message, http_code=201, error_code="CREATED", data=data)


class Accepted(BaseHTTPException):
    def __init__(self, message="Accepted", data=None):
        super().__init__(message, http_code=202, error_code="ACCEPTED", data=data)


class BadRequest(BaseHTTPException):
    def __init__(self, message="Bad Request", data=None):
        super().__init__(message, http_code=400, error_code="BAD_REQUEST", data=data)


class NotFound(BaseHTTPException):
    def __init__(self, message="Not Found", data=None):
        super().__init__(message, http_code=404, error_code="NOT_FOUND", data=data)


class InternalServerError(BaseHTTPException):
    def __init__(self, message="Internal Server Error", data=None):
        super().__init__(message, http_code=500, error_code="INTERNAL_ERROR", data=data)
