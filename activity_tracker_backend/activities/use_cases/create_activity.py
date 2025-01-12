# activities/use_cases/create_activity.py

from activities.data.repositories.activity_repository_impl import ActivityRepository
from activities.data.models import ActivityModel

class CreateActivityUseCase:
    def __init__(self, repository: ActivityRepository):
        self.repository = repository

    def execute(self, user_id: int, title: str, description: str) -> ActivityModel:
        return self.repository.create_activity(user_id, title, description)
