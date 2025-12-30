from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import ObjectId ,json_util
import os
from dotenv import load_dotenv
from typing import List, Dict


class Interactor:
    def __init__(self):
        load_dotenv()
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.name = os.getenv("DB_NAME")
        self.db = None
        self.collection = None

    def load_contacts(self):
        try:
            client = MongoClient(f"mongodb://{self.host}:{self.port}/",serverSelectionTimeoutMS=5000)
            client.admin.command("ping")
            self.db = client[self.name]
            self.collection = client[self.name].contacts
            return "Successfully connected to MongoDB!"

        except ConnectionFailure as e:
            return f"Failed to connect to MongoDB:\n{e}"

    def get_all_contacts(self) -> List[Dict] | bool:
        if self.db is None:
            self.load_contacts()

        if self.collection is None:
            return False
        else:
            return list(self.collection.find())

    def create_contact(self,contact_data: dict) -> str | bool:
        if self.db is None:
            self.load_contacts()

        if self.collection is None:
            return False
        else:
            result = self.collection.insert_one(contact_data)
            return result.inserted_id

    def update_contact(self,id: str, contact_data: dict) -> bool:
        if self.db is None:
            self.load_contacts()

        if self.collection is None:
            return False
        else:
            self.collection.replace_one({"_id":ObjectId(id)},contact_data)
            return True

    def delete_contact(self,id: str)-> bool:
        if self.db is None:
            self.load_contacts()

        if self.collection is None:
            return False
        else:
            self.collection.delete_many({"_id":ObjectId(id)})
            return True





