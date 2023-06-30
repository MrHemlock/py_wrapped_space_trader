from os import getenv
import requests as r

from dotenv import load_dotenv


load_dotenv()
TOKEN = getenv("TOKEN")

BASE_URL = "https://api.spacetraders.io/v2"
HEADERS = {"Content-Type": "application/json", "Authorization": f"Bearer {TOKEN}"}


 # r.post()
