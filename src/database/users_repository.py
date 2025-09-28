from datetime import datetime, UTC

from bson import ObjectId
from pymongo.synchronous.database import Database

from models.user import CreateUser
from src.database.user_interface import UserInterface


class Users(UserInterface):
    def __init__(self, db: Database):
        self.db = db
        self.user_collection = self.db.get_collection("users")
        self.tokens_blacklisted =self.db.get_collection("blacklisted_tokens")
        self.tokens_blacklisted.create_index(
            [('date_added', 1)], expireAfterSeconds=1800
        )

    def add_user(self, user: CreateUser):
        user_data = user.model_dump()
        new_id = self.user_collection.insert_one(user_data).inserted_id
        user_data["id"] = str(new_id)
        return user_data



    def get_user_by_id(self, user_id: str):
        result = self.user_collection.find_one({"_id": ObjectId(user_id)})
        if result is None:
            return None
        result["id"] = str(result["_id"])
        return result

    def get_user_by_email(self, email: str):
        result = self.user_collection.find_one({"email": email})
        if result is None:
            return None
        result["id"] = str(result["_id"])
        return result


    def user_blacklist_token(self, token: str):
        self.tokens_blacklisted.insert_one({
            "token": token,
            'date_added': datetime.now(UTC),
        })

    def check_blacklisted_token(self, token: str):
        return self.tokens_blacklisted.find_one({"token": token}) is not None