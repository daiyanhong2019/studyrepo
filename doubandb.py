from pymongo import MongoClient
from pymongo import InsertOne

class DoubanDb:
    def __init__(self):
        self.conn = MongoClient("127.0.0.1:27017", maxPoolSize=None)
        self.db = self.conn.douban
        self.myset = self.db.films

    def insert(self,data):
        print("insert data:")
        self.myset.insert_many(data)

    def delete(self):
        print("delete...")
        self.db.dropDatabase()