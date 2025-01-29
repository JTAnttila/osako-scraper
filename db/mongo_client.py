from pymongo import MongoClient
from ..config.settings import MONGO_URI, DB_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def save_to_mongodb(menu_items, restaurant_name):
    if menu_items:
        for item in menu_items:
            item['restaurant'] = restaurant_name
            collection.insert_one(item)
        print(f"Successfully saved {len(menu_items)} items for {restaurant_name}.")
    else:
        print(f"No menu items found for {restaurant_name}.")