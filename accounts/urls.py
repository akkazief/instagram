from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from accounts.views import RegisterView, profile, UserSearchView

app_name = "accounts"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "login/", LoginView.as_view(template_name="accounts/login.html"), name="login"
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("search/", UserSearchView.as_view(), name="search"),
    path("profile/<str:username>/", profile, name="profile"),
]
