from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_daily_email, send_deadline_passed_email


# Create your views here.
def send_daily(request):
    # Testing purposes only
    send_daily_email()
    return HttpResponse("Daily email sent!")


def check_deadlines(request):
    # Testing purposes only
    send_deadline_passed_email()
    return HttpResponse("Deadline passed emails sent!")
