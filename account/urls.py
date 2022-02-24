from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from .views import Dashboard

app_name = 'account'
urlpatterns = [
    path('',
         Dashboard.as_view(),
         name='dashboard'),
    path('login/',
         auth_views.LoginView.as_view(),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done')
]
