from django.urls import path

from . import views

urlpatterns = [
    path('send_daily', views.send_daily, name="send_daily"),
]
