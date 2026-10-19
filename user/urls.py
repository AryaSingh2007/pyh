from django.urls import path
from . import views

urlpatterns=[
    path("index/",views.index), 
    path("",views.index), 
    path("contact/",views.contact),
    path("about/",views.about),
    path("gallery/",views.gallery),
    path("team/",views.team),
    path("profile/",views.profile),
    path("uprofile/",views.uprofile),
    path("registration/",views.registration),
    path("login/",views.login),
    path("dashboard/",views.dashboard),
    path("products/",views.products),
    path("cart/",views.cart),
]