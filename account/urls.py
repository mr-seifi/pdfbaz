from django.contrib.auth import views as auth_views
from django.urls import path

from .views import Dashboard

app_name = 'account'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', Dashboard.as_view(), name='dashboard'),
]
