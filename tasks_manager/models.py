from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
    # SET_NULL because if user is deleted, someone else needs to complete task anyway
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title
