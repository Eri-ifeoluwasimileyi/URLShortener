from exceptions.user_exceptions import *
from src.database.user_interface import UserInterface
from src.models.user import CreateUser, LoginUser
from src.utils.password import hash_password, verify_password


class UserService:
    def __init__(self, users: UserInterface):
        self.users = users

    def register_user(self, user: CreateUser):
        self.__check_email(user.email)

        user.password = hash_password(user.password)
        return self.users.add_user(user)

    def verify_user(self, user: LoginUser):
        found_user = self.users.get_user_by_email(user.email)
        if found_user is None:
            raise UserNotFoundError('User not found', 404)
        if verify_password(
                plain_password=user.password,
                hashed_password=found_user['password']
         ):
            return found_user
        raise IncorrectPasswordError('Incorrect password', 404)

    def __check_email(self, email: str):
        if self.users.get_user_by_email(email) is not None:
            raise UserAlreadyExistsError(f"User {email} already exists", 400)

    def blacklist_token(self, token: str):
        self.users.user_blacklist_token(token)

    def is_jti_blacklisted(self, token: str):
        return self.users.check_blacklisted_token(token)
