import pymongo
from pymongo.errors import ConnectionFailure
from bson import ObjectId
import os
from dotenv import load_dotenv
from typing import List, Dict
from contact import Contact


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
            client = pymongo.MongoClient(f"mongodb://{self.host}:{self.port}/",serverSelectionTimeoutMS=7000)
            client.admin.command("ping")
            self.db = client[self.name]
            self.collection = client[self.name].contacts
            self.collection.create_index([("phone_number", pymongo.ASCENDING)], unique=True)
            print("Successfully connected to MongoDB!")

        except ConnectionFailure as e:
            print(f"Failed to connect to MongoDB:\n{e}")
            raise ConnectionFailure

    def get_all_contacts(self) -> List[Dict] :
        if self.db is None:
            self.load_contacts()

        result = []
        contacts =  list(self.collection.find())
        for c in contacts:
            contact_object = Contact(c["first_name"],c["last_name"],c["phone_number"],str(c["_id"]))
            result.append(contact_object.contact_to_dict())
        return result


    def create_contact(self,contact_data: dict) -> str :
        if self.db is None:
            self.load_contacts()
        result = self.collection.insert_one(contact_data)
        return str(result.inserted_id)

    def update_contact(self,id: str, contact_data: dict) -> bool:
        if self.db is None:
            self.load_contacts()
        self.collection.replace_one({"_id":ObjectId(id)},contact_data)
        return True

    def delete_contact(self,id: str)-> bool:
        if self.db is None:
            self.load_contacts()
        self.collection.delete_many({"_id":ObjectId(id)})
        return True






