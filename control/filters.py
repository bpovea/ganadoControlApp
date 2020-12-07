import django_filters
from .models import *

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name':['exact'],
            'code':['exact'],
            'onhand_qty':['exact','gt','lt','gte','lte'],
            'category_id':['exact']
        }

class LivestockFilter(django_filters.FilterSet):
    class Meta:
        model = Livestock
        fields = {
            'code':['exact'],
            'weight_initial':['exact','gt','lt','gte','lte'],
            'weight_current':['exact','gt','lt','gte','lte']
        }

class IncomeFilter(django_filters.FilterSet):
    class Meta:
        model = Income
        fields = {
            'product_id':['exact'],
            'datetime_in':['exact','gt','lt','gte','lte'],
            'quantity':['exact','gt','lt','gte','lte']
        }

class OutcomeFilter(django_filters.FilterSet):
    class Meta:
        model = Outcome
        fields = {
            'product_id':['exact'],
            'livestock_id':['exact'],
            'datetime_out':['exact','gt','lt','gte','lte'],
            'quantity':['exact','gt','lt','gte','lte']
        }