from django.conf.urls import url
from django.urls import path, include
from .views import RegisterView, GoogleLogin, GithubLogin, LoginView
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    # url(r"^", include("rest_auth.urls")),
    url(r"^refresh/", refresh_jwt_token),
    url(r"^registration/", RegisterView.as_view(), name="register"),
    url(r"^login/", LoginView.as_view(), name="login"),
    url(r"^login/google/$", GoogleLogin.as_view(), name="google_login"),
    url(r"^login/github/$", GithubLogin.as_view(), name="github_login"),
    url(
        r"^social/",
        include("allauth.socialaccount.urls"),
        name="socialaccount_signup",
    ),
]
