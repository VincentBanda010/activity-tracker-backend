# activities/domain/entities/activity.py

from dataclasses import dataclass
from datetime import date

@dataclass
class Activity:
    id: int
    user_id: int
    title: str
    description: str
    date: date
    created_at: date
