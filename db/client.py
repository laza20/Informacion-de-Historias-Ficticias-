from pymongo import MongoClient

db_client = MongoClient().local

client = MongoClient("mongodb://localhost:27017")
db_client = client["historias_ficticias"] 