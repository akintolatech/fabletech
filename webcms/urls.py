
from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.index, name="index"),
    path("menu/", views.menu, name="menu"),
    path("about/", views.about, name="about"),
]
