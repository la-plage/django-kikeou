from django.urls import path

from kikeou import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
]
