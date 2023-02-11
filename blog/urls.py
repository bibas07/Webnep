from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboardView, name="dashboard"),
    path('post/file-upload', views.model_form_upload, name="file-upload"),
    path("posts/<int:id>/delete", views.postDelete, name="post_delete"),
]