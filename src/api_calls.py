from os import getenv
from pprint import pprint

import dotenv
import requests

from pydantic_models import Status


dotenv.load_dotenv()

BASE_URL = "https://api.spacetraders.io/v2/"
TOKEN = getenv("TOKEN")

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": TOKEN,
}


def get_status():
    response = requests.get(BASE_URL, headers=HEADERS)
    status = Status(**response.json())
    return status
