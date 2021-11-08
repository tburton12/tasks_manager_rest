from celery import shared_task
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
                  # recipient_list=['wrzesien65@gmail.com'])
                  recipient_list=[user.email])

    return None
