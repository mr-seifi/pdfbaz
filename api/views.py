from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.postgres.search import SearchRank
from store.models import Author, Publisher, Book
from .serializers import AuthorSerializer, PublisherSerializer, BookSerializer, \
    MyTokenObtainPairSerializer, RegisterSerializer
from django.db.models import F


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny, )
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAuthenticated]


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['year', 'language', 'topic']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        search_param = self.request.GET.get('search')
        return Book.objects.filter(document=search_param)\
            .annotate(rank=SearchRank(F('document'), search_param))\
            .order_by('-rank') if search_param else Book.objects.all()


