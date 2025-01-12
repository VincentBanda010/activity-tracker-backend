# activities/use_cases/get_activities.py

from typing import List
from activities.domain.entities.activity import Activity
from activities.domain.repositories import ActivityRepositoryInterface

class GetActivitiesUseCase:
    def __init__(self, repository: ActivityRepositoryInterface):
        self.repository = repository

    def execute(self, user_id: int) -> List[Activity]:
        return self.repository.get_activities(user_id)
