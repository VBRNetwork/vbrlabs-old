from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from django.http import JsonResponse
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from rest_framework.views import APIView
from django.http import JsonResponse
from dry_rest_permissions.generics import DRYPermissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import (
    HomePageContentSerializer,
    PartnersContentSerializer,
    ServicesContentSerializer,
    AboutUsContentSerializer,
    BlockchainContentSerializer,
    TechnologiesContentSerializer,
    ProjectsSerializer,
    TeamMembersSerializer,
    TeamSerializer,
    SubscribersSerializer,
)
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
from django.db.models import Sum

url_listings = (
    "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
)
parameters_listings = {'symbol': 'BTC,ETH,SLBZ,AURORA'}
headers_listings = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "e53ffdd8-c5ad-4220-8c20-39ed048d0a2e",
}

url_convert = "https://rest.coinapi.io/v1/exchangerate/"
headers_convert = {
    "Accepts": "application/json",
    "X-CoinAPI-Key": "8409B43E-B0F4-424A-A804-E740FA548787",
}

class HomePageContentListAPIView(ListAPIView):
    queryset = HomePageContent.objects.all()
    serializer_class = HomePageContentSerializer
    permission_classes = [AllowAny]
    pagination_class = None
    filter_backends = ()
    filter_fields = ()
    search_fields = ()
    ordering_fields = ()
    ordering = ()
    extra_kwargs = {}
    lookup_field = "slug"
    lookup_url_kwarg = "slug"

    # def get_queryset(self):
    #     return self.queryset.filter(is_active=True)

class SubscribersListAPIView(ListCreateAPIView):
    queryset = Subscribers.objects.all()
    serializer_class = SubscribersSerializer
    permission_classes = [AllowAny]
    pagination_class = None
    filter_backends = ()
    filter_fields = ()
    search_fields = ()
    ordering_fields = ()
    ordering = ()
    extra_kwargs = {}
    lookup_field = "email"
    lookup_url_kwarg = "email"

    
class PartnersContentListAPIView(ListAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersContentSerializer
    permission_classes = [AllowAny]
    pagination_class = None
    filter_backends = ()
    filter_fields = ()
    search_fields = ()
    ordering_fields = ()
    ordering = ()
    extra_kwargs = {}
    lookup_field = "slug"
    lookup_url_kwarg = "slug"

    # def get_queryset(self):
    #     return self.queryset.filter(is_active=True)

    
class ServicesContentListAPIView(ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesContentSerializer
    permission_classes = [AllowAny]
    pagination_class = None
    filter_backends = ()
    filter_fields = ()
    search_fields = ()
    ordering_fields = ()
    ordering = ()
    extra_kwargs = {}
    lookup_field = "slug"
    lookup_url_kwarg = "slug"

    # def get_queryset(self):
    #     return self.queryset.filter(is_active=True)

class AboutUsContentListAPIView(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsContentSerializer
    permission_classes = [AllowAny]
    pagination_class = None
    filter_backends = ()
    filter_fields = ()
    search_fields = ()
    ordering_fields = ()
    ordering = ()
    extra_kwargs = {}
    lookup_field = "slug"
    lookup_url_kwarg = "slug"

    # def get_queryset(self):
    #     return self.queryset.filter(is_active=True)

class BlockchainContentListAPIView(ListAPIView):
    queryset = BlockchainContent.objects.all()
    serializer_class = BlockchainContentSerializer
    permission_classes = [AllowAny]
    pagination_class = None
    filter_backends = ()
    filter_fields = ()
    search_fields = ()
    ordering_fields = ()
    ordering = ()
    extra_kwargs = {}
    lookup_field = "slug"
    lookup_url_kwarg = "slug"

    # def get_queryset(self):
    #     return self.queryset.filter(is_active=True)

class TechnologiesListAPIView(ListAPIView):
    queryset = Technologies.objects.all()
    serializer_class = TechnologiesContentSerializer
    permission_classes = [AllowAny]
    pagination_class = None
    filter_backends = ()
    filter_fields = ()
    search_fields = ()
    ordering_fields = ()
    ordering = ()
    extra_kwargs = {}
    lookup_field = "slug"
    lookup_url_kwarg = "slug"

    # def get_queryset(self):
    #     return self.queryset.filter(is_active=True)

class ProjectsListAPIView(ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [AllowAny]
    pagination_class = None
    filter_backends = ()
    filter_fields = ()
    search_fields = ()
    ordering_fields = ()
    ordering = ()
    extra_kwargs = {}
    lookup_field = "slug"
    lookup_url_kwarg = "slug"

    # def get_queryset(self):
    #     return self.queryset.filter(is_active=True)

class TeamMembersListAPIView(APIView):
    serializer_class = TeamMembersSerializer
    permission_classes = [AllowAny]
    pagination_class = None
    filter_backends = ()
    filter_fields = ()
    search_fields = ()
    ordering_fields = ()
    ordering = ()
    extra_kwargs = {}
    lookup_field = "slug"
    lookup_url_kwarg = "slug"

    def get(self, request, *args, **kwargs):
        
        query = TeamMembers.objects.aggregate(
            web_p = Sum('team_member_web_projects_completed'),
            mobile_p = Sum('team_member_mobile_projects_completed'),
        blockchain_p = Sum('team_member_blockchain_projects_completed'),
        )

        return JsonResponse(query, safe=False)

class GetExchangeListinngsListAPIView(APIView):

    permission_classes = []
    serializer_class = []
    authentication_classes = []
    pagination_class = None

    session = Session()

    def get(self, request, *args, **kwargs):

        self.session.headers.update(headers_listings)

        try:
            response = self.session.get(url_listings, params=parameters_listings)
            data = json.loads(response.text)
            # jsonified_data = json.dumps(data, sort_keys=True, indent=2)
            print(data)
            return JsonResponse(data, safe=False)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            return JsonResponse(
                status=400, data={"error": "Request timed out."}
            )

class TeamListAPIView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [AllowAny]
    pagination_class = None
    filter_backends = ()
    filter_fields = ()
    search_fields = ()
    ordering_fields = ()
    ordering = ()
    extra_kwargs = {}
    lookup_field = "slug"
    lookup_url_kwarg = "slug"

    # def get_queryset(self):
    #     return self.queryset.filter(is_active=True)
