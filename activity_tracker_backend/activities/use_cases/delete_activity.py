# activities/use_cases/delete_activity.py

from activities.domain.repositories import ActivityRepositoryInterface

class DeleteActivityUseCase:
    def __init__(self, repository: ActivityRepositoryInterface):
        self.repository = repository

    def execute(self, activity_id: int) -> None:
        self.repository.delete_activity(activity_id)
