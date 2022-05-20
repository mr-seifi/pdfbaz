from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'api'

router = DefaultRouter()
router.register(r'author', views.AuthorViewSet)
router.register(r'publisher', views.PublisherViewSet)
router.register(r'book', views.BookViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title='API',
        default_version='v1'
    ),
    public=True
)

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('login/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('download/', views.DownloadBookViewSet.as_view(), name='linker'),
    path('download/<str:book_hash>/', views.RedirectBookFileViewSet.as_view(), name='download_book'),
    path('', include(router.urls)),
]
