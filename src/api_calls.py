from os import getenv

import dotenv
import requests

from api_models import (
    Status,
    RegisterAgentModel
)


dotenv.load_dotenv()

BASE_URL = "https://api.spacetraders.io/v2/"
TOKEN = getenv("TOKEN")
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {TOKEN}",
}


def get_status():
    response = requests.get(BASE_URL, headers=HEADERS)
    status = Status(**response.json())
    return status


def register_new_agent(
):
    ...
