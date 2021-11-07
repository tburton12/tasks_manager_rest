from rest_framework import viewsets, status

from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import UserSerializer, TaskSerializer
from .models import User, Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'], url_name="tasks")
    def tasks(self, request, pk):
        single_user = User.objects.get(id=pk)
        tasks = single_user.task_set.all()
        serializer = TaskSerializer(tasks, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
