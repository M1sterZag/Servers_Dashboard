from django.urls import path
from . import views

app_name = "cards"

urlpatterns = [
    path("", views.index, name="index"),
    path("servers/", views.servers, name="servers"),
    path("new_server/", views.new_server, name="new_server"),
    path("delete_server/<int:server_id>/", views.delete_server, name="delete_server"),
    path('edit_server/<int:server_id>/', views.edit_server, name='edit_server'),
]
