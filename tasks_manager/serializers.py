from rest_framework import serializers

from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    owner_name = serializers.SerializerMethodField()

    @staticmethod
    def get_owner_name(obj):
        if obj.owner:  # It's allowed for task to have no owner
            return '{} {}'.format(obj.owner.first_name, obj.owner.last_name)
        return None

    owner_url = serializers.HyperlinkedIdentityField(view_name='user-detail')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'is_finished', 'owner_name', 'owner_url', 'deadline']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    unfinished_tasks = serializers.SerializerMethodField('count_unfinished_tasks')

    all_tasks = serializers.HyperlinkedIdentityField(view_name='user-tasks')

    @staticmethod
    def count_unfinished_tasks(user):
        return user.task_set.all().filter(is_finished=False).count()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'unfinished_tasks', 'all_tasks')
