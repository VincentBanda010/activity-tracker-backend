# activities/views/activity_views.py

from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from activities.data.serializers import ActivitySerializer
from activities.data.models import ActivityModel
from activities.domain.repositories import ActivityRepositoryInterface
from activities.use_cases.get_activities import GetActivitiesUseCase
from activities.use_cases.create_activity import CreateActivityUseCase
from activities.use_cases.update_activity import UpdateActivityUseCase
from activities.use_cases.delete_activity import DeleteActivityUseCase
from activities.data.repositories.activity_repository_impl import ActivityRepository
from activities.domain.entities.activity import Activity
from rest_framework.response import Response
from rest_framework import status

class ActivityViewSet(viewsets.ViewSet):

    def list(self, request):
        repository = ActivityRepository()
        use_case = GetActivitiesUseCase(repository)
        activities = use_case.execute(user_id=request.user.id)
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

    def create(self, request):
        repository = ActivityRepository()
        use_case = CreateActivityUseCase(repository)
        title = request.data.get('title')
        description = request.data.get('description')
        activity = use_case.execute(user_id=request.user.id, title=title, description=description)
        serializer = ActivitySerializer(activity)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        # Implement retrieve logic using use cases
        pass

    def update(self, request, pk=None):
        repository = ActivityRepository()
        use_case = UpdateActivityUseCase(repository)
        title = request.data.get('title')
        description = request.data.get('description')
        activity = Activity(
            id=pk,
            user_id=request.user.id,
            title=title,
            description=description,
            date=None,  # Handle date accordingly
            created_at=None  # Handle created_at accordingly
        )
        updated_activity = use_case.execute(activity)
        serializer = ActivitySerializer(updated_activity)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        repository = ActivityRepository()
        use_case = DeleteActivityUseCase(repository)
        use_case.execute(activity_id=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
