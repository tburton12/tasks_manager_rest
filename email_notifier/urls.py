from django.urls import path

from . import views

urlpatterns = [
    path('send_daily', views.send_daily, name="send_daily"),
    path('check_deadlines', views.check_deadlines, name="check_deadlines")
]
