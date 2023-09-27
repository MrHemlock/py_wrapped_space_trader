from __future__ import annotations

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
)
from pydantic.alias_generators import to_camel

from pydantic_models import (
    FactionSymbols,
)


class ApiModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)


# API endpoint response models
class Status(ApiModel):
    status: str
    version: str
    reset_date: str
    description: str
    stats: Stats
    leaderboards: LeaderBoards
    server_resets: ServerReset
    announcements: list[Announcement]
    links: list[Link]


class Stats(ApiModel):
    agents: int
    ships: int
    systems: int
    waypoints: int


class LeaderBoards(ApiModel):
    most_credits: list[AgentCredits]
    most_submitted_charts: list[AgentCharts]


class AgentCredits(ApiModel):
    agent_symbol: str
    credits: int


class AgentCharts(ApiModel):
    agent_symbol: str
    chart_count: int


class ServerReset(ApiModel):
    next: str
    frequency: str


class Announcement(ApiModel):
    title: str
    body: str


class Link(ApiModel):
    name: str
    url: str


class RegisterAgentModel(ApiModel):
    faction: FactionSymbols
    symbol: str = Field(min_length=3, max_length=14)
    email: EmailStr
