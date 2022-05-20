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
from rest_framework.views import APIView
from payment.models import OrderBook
from linker.tasks import generate_download_url
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from store.services.libgen_service import LibgenService
from linker.tasks import get_book_id
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


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
        return Book.objects.filter(document=search_param) \
            .annotate(rank=SearchRank(F('document'), search_param)) \
            .order_by('-rank') if search_param else Book.objects.all()


class DownloadBookViewSet(APIView):
    """
        Download a book via book_id<int> parameter
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[Parameter(name='book_id',
                                                      in_='path',
                                                      description='Book identity document',
                                                      required=True,
                                                      type='int')])
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=request.query_params.get('book_id'))
        if not OrderBook.has_payment(user=request.user,
                                     book=book):
            return Response({'message': 'You don\'t have permissions to access this page!'}, status=403)

        return Response(f'http://127.0.0.1:8000/api/download/{generate_download_url(book=book)}/')


class RedirectBookFileViewSet(APIView):
    """
        Redirect a book hash to real file
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=get_book_id(kwargs.get('book_hash')))
        if not OrderBook.has_payment(user=request.user,
                                     book=book):
            return Response({'message': 'You don\'t have permissions to access this page!'}, status=403)

        filename = f'{LibgenService.get_book_identifier(book.__dict__)}.{book.extension}'
        response = FileResponse(book.file.open(), content_type=book.extension)
        response['Content-Length'] = book.filesize
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename

        return response


# TODO: Create a task which delete all book into the files in 00:00
