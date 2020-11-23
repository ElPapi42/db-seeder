from pymongo import MongoClient

from seeder import settings


client = MongoClient(settings.DB_URL)

db = client[settings.DB_NAME]
