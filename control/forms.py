from django import forms

from .models import Product, CategoryProduct

from bootstrap_modal_forms.forms import BSModalModelForm
from bootstrap_modal_forms.forms import BSModalForm


class ProductModelForm(BSModalModelForm):
    class Meta:
        model = Product
        fields = ['code', 'name', 'onhand_qty','category_id']
        labels = {
            'code': 'Código',
            'name': 'Nombre',
            'onhand_qty':'Disponible',
            'category_id':'Categoría'
        }


class ProductUpdateModelForm(BSModalModelForm):
    class Meta:
        model = Product
        fields = ['code', 'name', 'category_id']
        labels = {
            # 'code': _('código'),
            'code': 'Código',
            'name': 'Nombre',
            'category_id':'Categoría'
        }


class ProductFilterForm(BSModalForm):
    category_id = forms.ModelChoiceField(queryset=CategoryProduct.objects.all(),required=False,label='Categoría')
    name = forms.CharField(max_length=80,required=False,label="Nombre")
    code = forms.CharField(max_length=10,required=False)
    onhand_qty = forms.FloatField(label='Disponible = a')
    onhand_qty__gt = forms.FloatField(label='Disponible > a')
    onhand_qty__gte = forms.FloatField(label='Disponible >= a')
    onhand_qty__lt = forms.FloatField(label='Disponible < a')
    onhand_qty__lte = forms.FloatField(label='Disponible <= a')


    class Meta:
        fields = [
            'code','category_id','name',
            'onhand_qty','onhand_qty__gt','onhand_qty__lt',
            'onhand_qty__gte','onhand_qty__lte','clear']