

from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.index),
    # path("feb", views.celeb)
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.challenge, name="month_challenge")


]
