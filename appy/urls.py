

from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.index),
    # path("feb", views.celeb)
    path("<month>", views.celeb)

]
