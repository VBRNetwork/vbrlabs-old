from django.conf.urls import url
from django.urls import path
from .views import UserListView, UserView

urlpatterns = [
    path(
        "<slug:username>",
        UserView.as_view(),
        name="profile",
    ),
]
