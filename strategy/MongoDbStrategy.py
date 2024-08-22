from pymongo import MongoClient
from interfaces import IDatabaseStrategy

class MongoStrategy(IDatabaseStrategy):
    
    def __init__(self, mongo_url: str, db_name: str):
        self.mongo_url = mongo_url
        self.db_name = db_name
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(self.mongo_url)
            self.db = self.client[self.db_name]
        except Exception as e:
            raise ConnectionError(f"Failed to connect to MongoDB: {e}")

    def get_all(self, collection_name: str):
        try:
            return list(self.db[collection_name].find())
        except Exception as e:
            raise RuntimeError(f"Failed to retrieve data: {e}")

    def save(self, collection_name: str, data: dict):
        try:
            self.db[collection_name].insert_one(data)
        except Exception as e:
            raise RuntimeError(f"Failed to save data: {e}")

    def find_one(self, collection_name: str, query: dict):
        try:
            return self.db[collection_name].find_one(query)
        except Exception as e:
            raise RuntimeError(f"Failed to find data: {e}")
