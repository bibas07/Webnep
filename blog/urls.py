from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboardView, name="dashboard"),
    path("posts/<int:id>/delete", views.postDelete, name="post_delete"),
]