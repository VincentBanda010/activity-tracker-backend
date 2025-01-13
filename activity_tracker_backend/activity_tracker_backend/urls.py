# activity_tracker_backend/activity_tracker_backend/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('activities.urls')),  # Routes to activities app
    path('api-auth/', include('rest_framework.urls')),  # Optional: Browsable API login/logout
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Removed
]
