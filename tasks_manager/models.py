from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Task(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
    # SET_NULL because if user is deleted, someone else needs to complete task anyway
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title
