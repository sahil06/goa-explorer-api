class DomainException(Exception):
    pass


class ValidationException(DomainException):
    def __init__(self, message: str):
        super().__init__(message)

class NotFoundException(DomainException):
    pass


