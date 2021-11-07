from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, TaskSerializer
from .models import User, Task


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'], url_name="tasks")
    def tasks(self, request, pk):
        """Returns ALL tasks related to given user id"""
        single_user = User.objects.get(id=pk)
        tasks = single_user.task_set.all()
        serializer = TaskSerializer(tasks, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_name="me", url_path="me/tasks")
    def my_tasks(self, request):
        """Returns ALL tasks related to authorized user"""
        pk = request.user.id
        single_user = User.objects.get(id=pk)
        tasks = single_user.task_set.all()
        serializer = TaskSerializer(tasks, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
