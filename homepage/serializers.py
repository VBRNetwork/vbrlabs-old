from rest_framework import serializers
from rest_framework_cache.registry import cache_registry
from main.serializers import CachedSerializerMixin
from .models import (
    HomePageContent,
    Partners,
    Services,
    AboutUs,
    BlockchainContent,
    Technologies,
    Projects,
    TeamMembers,
    Team,
    Subscribers,
)


class HomePageContentSerializer(
    serializers.ModelSerializer,
    CachedSerializerMixin):

    class Meta:
        model = HomePageContent
        fields = "__all__"

class SubscribersSerializer(
    serializers.ModelSerializer,
    CachedSerializerMixin):

    class Meta:
        model = Subscribers
        fields = "__all__"

class PartnersContentSerializer(
    serializers.ModelSerializer,
    CachedSerializerMixin):

    class Meta:
        model = Partners
        fields = "__all__"

class ProjectsSerializer(
    serializers.ModelSerializer,
    CachedSerializerMixin):

    project_partners = PartnersContentSerializer(many=True)

    class Meta:
        model = Projects
        fields = "__all__"

class TechnologiesContentSerializer(
    serializers.ModelSerializer,
    CachedSerializerMixin):

    class Meta:
        model = Technologies
        fields = "__all__"

class TeamMembersSerializer(
    serializers.ModelSerializer,
    CachedSerializerMixin):

    class Meta:
        model = TeamMembers
        fields = "__all__"

class TeamSerializer(
    serializers.ModelSerializer,
    CachedSerializerMixin):

    team_members = TeamMembersSerializer(many=True)
    projects = ProjectsSerializer(many=True)

    class Meta:
        model = Team
        fields = "__all__"

class ServicesContentSerializer(
    serializers.ModelSerializer,
    CachedSerializerMixin):

    technologies = TechnologiesContentSerializer(many=True)

    class Meta:
        model = Services
        fields = "__all__"

class AboutUsContentSerializer(
    serializers.ModelSerializer,
    CachedSerializerMixin):

    class Meta:
        model = AboutUs
        fields = "__all__"

class BlockchainContentSerializer(
    serializers.ModelSerializer,
    CachedSerializerMixin):

    class Meta:
        model = BlockchainContent
        fields = "__all__"