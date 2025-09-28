from database.db import get_db
from database.url_repository import URLRepository
from services.url_service import URLService
from src.database.users_repository import Users
from src.services.user_service import UserService

def get_url_repository():
    return URLRepository(db=get_db())

def get_users_repository():
    return Users(db=get_db())

def get_user_service():
    return UserService(get_users_repository())

def get_url_service():
    return URLService(urls=get_url_repository(), users=get_users_repository())
