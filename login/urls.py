from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
]
