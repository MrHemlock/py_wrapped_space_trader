from os import getenv

import dotenv
from requests_ratelimiter import (
    Duration,
    Limiter,
    LimiterSession,
    RequestRate,
)

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
STANDARD_RATE = RequestRate(2, Duration.SECOND)
BURST_RATE = RequestRate(10, Duration.SECOND * 10)
RATES = Limiter(STANDARD_RATE, BURST_RATE)
# session = LimiterSession(limiter=RATES, headers=HEADERS)


def get_status(session: LimiterSession) -> Status:
    response = session.get(BASE_URL, headers=HEADERS)
    status = Status(**response.json())
    return status


def register_new_agent(
):
    ...


if __name__ == "__main__":
    session = LimiterSession(limiter=RATES, headers=HEADERS)
