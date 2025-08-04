import os
from dotenv import load_dotenv, find_dotenv

from database.repository import DBRepository


load_dotenv(find_dotenv())

DB_URL = os.getenv("DB_URL")


repository = DBRepository(DB_URL)

