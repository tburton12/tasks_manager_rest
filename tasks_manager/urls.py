from django.urls import path, include
from rest_framework import routers

from tasks_manager.views import UserViewSet, TaskViewSet

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)
router.register(r'task', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
