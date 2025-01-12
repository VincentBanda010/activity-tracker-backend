# activities/data/repositories/activity_repository_impl.py

from typing import List
from activities.domain.repositories import ActivityRepositoryInterface
from activities.data.models import ActivityModel

class ActivityRepository(ActivityRepositoryInterface):

    def get_activities(self, user_id: int) -> List[ActivityModel]:
        return ActivityModel.objects.filter(user_id=user_id).order_by('-date')

    def create_activity(self, user_id: int, title: str, description: str) -> ActivityModel:
        return ActivityModel.objects.create(
            user_id=user_id,
            title=title,
            description=description
        )

    def update_activity(self, activity_id: int, title: str, description: str) -> ActivityModel:
        activity = ActivityModel.objects.get(id=activity_id, user_id=user_id)
        activity.title = title
        activity.description = description
        activity.save()
        return activity

    def delete_activity(self, activity_id: int) -> None:
        ActivityModel.objects.filter(id=activity_id).delete()
