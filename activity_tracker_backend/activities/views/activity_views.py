# activities/views/activity_views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from activities.data.serializers import ActivitySerializer
from activities.data.models import ActivityModel

class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = ActivityModel.objects.all().order_by('-date')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        activity = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            activity = ActivityModel.objects.get(pk=pk)
            serializer = self.get_serializer(activity)
            return Response(serializer.data)
        except ActivityModel.DoesNotExist:
            return Response({'error': 'Activity not found'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None, *args, **kwargs):
        partial = kwargs.pop('partial', False)  # Extract 'partial' from kwargs
        try:
            activity = ActivityModel.objects.get(pk=pk)
            serializer = self.get_serializer(activity, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except ActivityModel.DoesNotExist:
            return Response({'error': 'Activity not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            activity = ActivityModel.objects.get(pk=pk)
            activity.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ActivityModel.DoesNotExist:
            return Response({'error': 'Activity not found'}, status=status.HTTP_404_NOT_FOUND)
