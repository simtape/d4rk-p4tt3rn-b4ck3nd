import os

import pymongo
from dotenv import load_dotenv

load_dotenv()
DB_CONN = os.environ.get("DB_CONNECTION")
client = pymongo.MongoClient(DB_CONN)
db = client["DarkPattern"]
cookie_banner_collection = db["CookieBanners"]
collection_second_part= db["BannersSecondPart"]
