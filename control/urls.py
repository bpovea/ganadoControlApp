from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', login_required(views.index), name='index'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]

