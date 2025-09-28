from abc import ABC, abstractmethod

from models.user import CreateUser


class UserInterface(ABC):

    @abstractmethod
    def add_user(self, user: CreateUser) -> dict:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: str):
        pass

    @abstractmethod
    def get_user_by_email(self, email: str):
        pass

    @abstractmethod
    def user_blacklist_token(self, token: str):
        pass

    @abstractmethod
    def check_blacklisted_token(self, token: str):
        pass
