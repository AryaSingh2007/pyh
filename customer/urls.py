from django.urls import path
from . import views

urlpatterns=[
    path("index/",views.index),
    path("profile/",views.profile),
    path("logout/",views.logout),
]