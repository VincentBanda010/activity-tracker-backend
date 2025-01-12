# activities/domain/repositories.py

from abc import ABC, abstractmethod
from typing import List
from .entities.activity import Activity

class ActivityRepositoryInterface(ABC):

    @abstractmethod
    def get_activities(self, user_id: int) -> List[Activity]:
        pass

    @abstractmethod
    def create_activity(self, activity: Activity) -> Activity:
        pass

    @abstractmethod
    def update_activity(self, activity: Activity) -> Activity:
        pass

    @abstractmethod
    def delete_activity(self, activity_id: int) -> None:
        pass
