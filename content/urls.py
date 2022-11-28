from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path("", auth_views.LoginView.as_view(template_name="content/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="content/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("change-password/", auth_views.PasswordChangeView.as_view(template_name="content/change_password.html"), name="password_change"),
    path("change-password/done/", auth_views.PasswordChangeDoneView.as_view(template_name="content/change_password_done.html"), name="password_change_done"),
    path("profile/",views.profileView, name="profile"),
    path("update-profile/", views.updateProfile, name="update-profile"),



]