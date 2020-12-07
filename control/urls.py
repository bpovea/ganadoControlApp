from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', login_required(views.index), name='index'),
    path('products/', login_required(views.ProductListView.as_view()), name='products'),
    path('create/product/', login_required(views.ProductCreateView.as_view()), name='create_product'),
    path('update/product/<int:pk>', login_required(views.ProductUpdateView.as_view()), name='update_product'),
    path('delete/product/<int:pk>', login_required(views.ProductDeleteView.as_view()), name='delete_product'),
    path('filter/product/', login_required(views.ProductFilterView.as_view()), name='filter_product'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]

