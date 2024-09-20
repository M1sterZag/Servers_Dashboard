from django.urls import path
from . import views

app_name = "cards"

urlpatterns = [
    path("", views.index, name="index"),
    path("servers/", views.servers, name="servers")
]
