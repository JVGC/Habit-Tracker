from abc import ABC


class UseCase(ABC):
    @staticmethod
    def execute():
        pass


class UseCaseError(BaseException):
    def __init__(self, message, status) -> None:
        self.status = status
        self.message = message
