from django.conf.urls import url
from django.urls import include, path
from .views import (
    HomePageContentListAPIView,
    PartnersContentListAPIView,
    ServicesContentListAPIView,
    AboutUsContentListAPIView,
    BlockchainContentListAPIView,
    TechnologiesListAPIView,
    ProjectsListAPIView,
    TeamMembersListAPIView,
    TeamListAPIView,
    GetExchangeListinngsListAPIView,
    SubscribersListAPIView,
)


urlpatterns = [
    url(
        r"home-content/$",
        HomePageContentListAPIView.as_view(),
        name="home-content",
    ),
    url(
        r"partners/$",
        PartnersContentListAPIView.as_view(),
        name="partners",
    ),
    url(
        r"services/$",
        ServicesContentListAPIView.as_view(),
        name="services",
    ),
    url(
        r"about/$",
        AboutUsContentListAPIView.as_view(),
        name="about",
    ),

    url(
        r"blockchain/$",
        BlockchainContentListAPIView.as_view(),
        name="blockchain",
    ),
    url(
        r"technologies/$",
        TechnologiesListAPIView.as_view(),
        name="technologies",
    ),
    url(
        r"projects/$",
        ProjectsListAPIView.as_view(),
        name="projects",
    ),
    url(
        r"team/members/$",
        TeamMembersListAPIView.as_view(),
        name="team_members",
    ),
    url(
        r"team/$",
        TeamListAPIView.as_view(),
        name="team",
    ),
    url(
        r"exchange/$",
        GetExchangeListinngsListAPIView.as_view(),
        name="exchange",
    ),
    url(
        r"subscribe/$",
        SubscribersListAPIView.as_view(),
        name="subscribe",
    ),

    
]
