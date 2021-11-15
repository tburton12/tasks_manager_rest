from celery import shared_task
from django.utils import timezone
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from tasks_manager.models import User, Task

from django.core.mail import send_mail


@shared_task(name="send_daily_email")
def send_daily_email():
    for user in User.objects.all():
        user_tasks = Task.objects.filter(owner=user)

        html_message = render_to_string('daily_email_body.html',
                                        context={'username': user.first_name, 'tasks': user_tasks})

        send_mail(subject="Task manager daily notification",
                  html_message=html_message,
                  message=strip_tags(html_message),
                  from_email="Task manager",
                  recipient_list=[user.email])

    return None


@shared_task(name="send_deadline_passed_email")
def send_deadline_passed_email():
    for task in Task.objects.all().filter(notification_sent=False):
        # If deadline has passed and email wasn't sent
        if task.deadline < timezone.now():
            # Task needs to have an owner
            if task.owner:
                html_message = render_to_string('deadline_passed_email.html',
                                                context={'username': task.owner.first_name, 'task_title': task.title,
                                                         'task_deadline': task.deadline})

                send_mail(subject="Time for your task has left!",
                          html_message=html_message,
                          message=strip_tags(html_message),
                          from_email="Task manager",
                          recipient_list=[task.owner.email])

                task.notification_sent = True
                task.save()

    return None
