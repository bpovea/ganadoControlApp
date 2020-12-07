import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name':['exact'],
            'code':['exact'],
            'onhand_qty':['exact','gt','lt','gte','lte'],
            'category_id':['exact']
        }