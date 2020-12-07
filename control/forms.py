from django import forms

from .models import *

from bootstrap_modal_forms.forms import BSModalModelForm
from bootstrap_modal_forms.forms import BSModalForm

from datetime import date, datetime

# Product Forms

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
    onhand_qty = forms.FloatField(label='Disponible = a',required=False)
    onhand_qty__gt = forms.FloatField(label='Disponible > a',required=False)
    onhand_qty__gte = forms.FloatField(label='Disponible >= a',required=False)
    onhand_qty__lt = forms.FloatField(label='Disponible < a',required=False)
    onhand_qty__lte = forms.FloatField(label='Disponible <= a',required=False)


    class Meta:
        fields = [
            'code','category_id','name',
            'onhand_qty','onhand_qty__gt','onhand_qty__lt',
            'onhand_qty__gte','onhand_qty__lte','clear']


# Livestock Forms

class LivestockModelForm(BSModalModelForm):
    optional_date = forms.DateField(help_text='* opcional, la fecha servirá de histórico al peso si difiere del actuál.',
                                    label='Fecha p. inicial', widget=forms.DateInput(attrs={'type': 'date'}),
                                    required=False,initial=date.today)
    class Meta:
        model = Livestock
        fields = ['code', 'weight_initial','optional_date','weight_current']
        labels = {
            'code': 'Código',
            'weight_initial':'Peso inicial',
            'weight_current':'Peso Actual'
        }


class LivestockUpdateModelForm(BSModalModelForm):
    class Meta:
        model = Livestock
        fields = ['code','weight_current']
        labels = {
            'code': 'Código',
            'weight_current':'Nuevo Peso Actual'
        }


class LivestockFilterForm(BSModalForm):
    code = forms.CharField(max_length=10,required=False)
    weight_initial = forms.FloatField(label='P. Inicial = a',required=False)
    weight_initial__gt = forms.FloatField(label='P. Inicial > a',required=False)
    weight_initial__gte = forms.FloatField(label='P. Inicial >= a',required=False)
    weight_initial__lt = forms.FloatField(label='P. Inicial < a',required=False)
    weight_initial__lte = forms.FloatField(label='P. Inicial <= a',required=False)
    weight_current = forms.FloatField(label='P. Actual = a',required=False)
    weight_current__gt = forms.FloatField(label='P. Actual > a',required=False)
    weight_current__gte = forms.FloatField(label='P. Actual >= a',required=False)
    weight_current__lt = forms.FloatField(label='P. Actual < a',required=False)
    weight_current__lte = forms.FloatField(label='P. Actual <= a',required=False)


    class Meta:
        fields = [
            'code',
            'weight_initial','weight_initial__gt','weight_initial__lt',
            'weight_initial__gte','weight_initial__lte',
            'weight_current','weight_current__gt','weight_current__lt',
            'weight_current__gte','weight_current__lte',
            'clear']


# Income Forms

class IncomeModelForm(BSModalModelForm):
    product_id = forms.ModelChoiceField(queryset=Product.objects.filter(active=True),required=True)
    commentary = forms.CharField(required=False)

    class Meta:
        model = Income
        fields = ['datetime_in', 'product_id','quantity','commentary']
        labels = {
            'datetime_in': 'F. de Ingreso',
            'product_id':'Producto',
            'quantity':'Cantidad',
            'comentary':'Comentario'
        }
        widgets = {
            'datetime_in': forms.DateTimeInput(attrs={'type': 'datetime-local', 'initial': datetime.now()}),
        }


class IncomeFilterForm(BSModalForm):
    product_id = forms.ModelChoiceField(queryset=Product.objects.filter(active=True),required=False)
    datetime_in = forms.DateField(label='F. Ingreso = a',required=False,widget=forms.DateInput(attrs={'type': 'date'}))
    datetime_in__gt = forms.DateField(label='F. Ingreso > a',required=False,widget=forms.DateInput(attrs={'type': 'date'}))
    datetime_in__gte = forms.DateField(label='F. Ingreso >= a',required=False,widget=forms.DateInput(attrs={'type': 'date'}))
    datetime_in__lt = forms.DateField(label='F. Ingreso < a',required=False,widget=forms.DateInput(attrs={'type': 'date'}))
    datetime_in__lte = forms.DateField(label='F. Ingreso <= a',required=False,widget=forms.DateInput(attrs={'type': 'date'}))
    quantity = forms.FloatField(label='Cantidad = a',required=False)
    quantity__gt = forms.FloatField(label='Cantidad > a',required=False)
    quantity__gte = forms.FloatField(label='Cantidad >= a',required=False)
    quantity__lt = forms.FloatField(label='Cantidad < a',required=False)
    quantity__lte = forms.FloatField(label='Cantidad <= a',required=False)


    class Meta:
        fields = [
            'product_id',
            'datetime_in','datetime_in__gt','datetime_in__lt',
            'datetime_in__gte','datetime_in__lte',
            'quantity','quantity__gt','quantity__lt',
            'quantity__gte','quantity__lte',
            'clear']


# Outcome Forms

class OutcomeModelForm(BSModalModelForm):
    product_id = forms.ModelChoiceField(queryset=Product.objects.filter(active=True),required=True)
    livestock_id = forms.ModelChoiceField(queryset=Livestock.objects.filter(active=True),required=True)
    commentary = forms.CharField(required=False)

    class Meta:
        model = Outcome
        fields = ['datetime_out', 'livestock_id','product_id','quantity','commentary']
        labels = {
            'datetime_out': 'F. de Ingreso',
            'product_id':'Producto',
            'quantity':'Cantidad',
            'comentary':'Comentario',
            'livestock_id':'Ganado'
        }
        widgets = {
            'datetime_out': forms.DateTimeInput(attrs={'type': 'datetime-local', 'initial': datetime.now()}),
        }


class OutcomeFilterForm(BSModalForm):
    product_id = forms.ModelChoiceField(queryset=Product.objects.filter(active=True),required=False)
    livestock_id = forms.ModelChoiceField(queryset=Livestock.objects.filter(active=True),required=False,label="Ganado")
    datetime_out = forms.DateField(label='F. Ingreso = a',required=False,widget=forms.DateInput(attrs={'type': 'date'}))
    datetime_out__gt = forms.DateField(label='F. Ingreso > a',required=False,widget=forms.DateInput(attrs={'type': 'date'}))
    datetime_out__gte = forms.DateField(label='F. Ingreso >= a',required=False,widget=forms.DateInput(attrs={'type': 'date'}))
    datetime_out__lt = forms.DateField(label='F. Ingreso < a',required=False,widget=forms.DateInput(attrs={'type': 'date'}))
    datetime_out__lte = forms.DateField(label='F. Ingreso <= a',required=False,widget=forms.DateInput(attrs={'type': 'date'}))
    quantity = forms.FloatField(label='Cantidad = a',required=False)
    quantity__gt = forms.FloatField(label='Cantidad > a',required=False)
    quantity__gte = forms.FloatField(label='Cantidad >= a',required=False)
    quantity__lt = forms.FloatField(label='Cantidad < a',required=False)
    quantity__lte = forms.FloatField(label='Cantidad <= a',required=False)


    class Meta:
        fields = [
            'product_id',
            'livestock_id',
            'datetime_in','datetime_in__gt','datetime_in__lt',
            'datetime_in__gte','datetime_in__lte',
            'quantity','quantity__gt','quantity__lt',
            'quantity__gte','quantity__lte',
            'clear']