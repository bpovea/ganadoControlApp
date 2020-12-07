from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', login_required(views.index), name='index'),
    # Productos
    path('products/', login_required(views.ProductListView.as_view()), name='products'),
    path('create/product/', login_required(views.ProductCreateView.as_view()), name='create_product'),
    path('update/product/<int:pk>', login_required(views.ProductUpdateView.as_view()), name='update_product'),
    path('delete/product/<int:pk>', login_required(views.ProductDeleteView.as_view()), name='delete_product'),
    path('filter/product/', login_required(views.ProductFilterView.as_view()), name='filter_product'),
    # Ganado
    path('livestocks/', login_required(views.LivestockListView.as_view()), name='livestocks'),
    path('create/livestock/', login_required(views.LivestockCreateView.as_view()), name='create_livestock'),
    path('update/livestock/<int:pk>', login_required(views.LivestockUpdateView.as_view()), name='update_livestock'),
    path('delete/livestock/<int:pk>', login_required(views.LivestockDeleteView.as_view()), name='delete_livestock'),
    path('filter/livestock/', login_required(views.LivestockFilterView.as_view()), name='filter_livestock'),
    # Ingresos
    path('incomes/', login_required(views.IncomeListView.as_view()), name='incomes'),
    path('create/income/', login_required(views.IncomeCreateView.as_view()), name='create_income'),
    path('delete/income/<int:pk>', login_required(views.IncomeDeleteView.as_view()), name='delete_income'),
    path('filter/income/', login_required(views.IncomeFilterView.as_view()), name='filter_income'),
    # Egresos
    path('outcomes/', login_required(views.OutcomeListView.as_view()), name='outcomes'),
    path('create/outcome/', login_required(views.OutcomeCreateView.as_view()), name='create_outcome'),
    path('delete/outcome/<int:pk>', login_required(views.OutcomeDeleteView.as_view()), name='delete_outcome'),
    path('filter/outcome/', login_required(views.OutcomeFilterView.as_view()), name='filter_outcome'),
    # Logout
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]

