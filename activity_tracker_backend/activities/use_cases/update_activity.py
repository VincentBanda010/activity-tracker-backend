# activities/use_cases/update_activity.py

from activities.domain.entities.activity import Activity
from activities.domain.repositories import ActivityRepositoryInterface

class UpdateActivityUseCase:
    def __init__(self, repository: ActivityRepositoryInterface):
        self.repository = repository

    def execute(self, activity: Activity) -> Activity:
        return self.repository.update_activity(activity)
