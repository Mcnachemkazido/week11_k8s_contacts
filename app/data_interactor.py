from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
from dotenv import load_dotenv
from typing import List, Dict

load_dotenv()
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")


class Interactor:
    def __init__(self):
        self.db = None

    def get_database(self):
        try:
            client = MongoClient(f"mongodb://{host}:{port}/")
            client.admin.command("ping")
            self.db = client.contacts_db
            return "✓ Successfully connected to MongoDB!"

        except ConnectionFailure as e:
            return f"✗ Failed to connect to MongoDB: {e}"

    def get_all_contacts(self) -> List[Dict]:
        if self.db is None:
            self.get_database()

        contacts_collection = self.db.contacts
        if contacts_collection is None:
            return []
        else:
            return list(contacts_collection.find())

    def create_contact(self,contact_data: dict) -> str:
        if self.db is None:
            self.get_database()

        contacts_collection = self.db.contacts
        if contacts_collection is None:
            return "no books_collection"
        else:
            result = contacts_collection.insert_one(contact_data)
            return result.inserted_id



i = Interactor()
print(i.create_contact({"first_name":"A","last_name":"a","phone_number":"aaaa"}))

