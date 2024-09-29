
from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.index, name="index"),
    path("shop/", views.shop, name="shop"),
    path("about/", views.about, name="about"),
]
