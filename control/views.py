from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages

from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView, BSModalFormView
from bootstrap_modal_forms.mixins import DeleteMessageMixin

from .models import *
from .forms import *
from .filters import *


def index(request):
    context = {'name':'Byron Povea'}
    return render(request,'index.html',context)


# Product Views

class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product/products.html'
    paginate_by = 5

    def get_queryset(self):
        f = ProductFilter(self.request.GET, queryset=Product.objects.filter(active=True))
        return f.qs


class ProductCreateView(BSModalCreateView):
    template_name = 'product/create_product.html'
    form_class = ProductModelForm
    success_message = 'Producto creado exitosamente.'
    success_url = reverse_lazy('products')


class ProductUpdateView(BSModalUpdateView):
    model = Product
    template_name = 'product/update_product.html'
    form_class = ProductUpdateModelForm
    success_message = 'Producto creado exitosamente.'
    success_url = reverse_lazy('products')


class ProductDeleteView(BSModalDeleteView):
    model = Product
    template_name = 'product/delete_product.html'
    success_message = 'Producto eliminado correctamente'
    success_url = reverse_lazy('products')

    def post(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.active = False
        self.object.save()
        return HttpResponseRedirect(success_url)


class ProductFilterView(BSModalFormView):
    template_name = 'product/filter_product.html'
    form_class = ProductFilterForm

    def form_valid(self, form):
        if 'clear' in self.request.POST:
            self.filter = ''
        else:
            self.filter = ''
            for k in self.request.POST.keys():
                if k=='csrfmiddlewaretoken':
                    continue
                elif self.request.POST[k] != '':
                    self.filter += ('?' if self.filter == '' else '&') + k + '=' + (str(form.cleaned_data[k].id) if k.endswith('_id') else str(form.cleaned_data[k]) )
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('products') + self.filter


# Livestock Views

class LivestockListView(generic.ListView):
    model = Livestock
    context_object_name = 'livestocks'
    template_name = 'livestock/livestocks.html'
    paginate_by = 5

    def get_queryset(self):
        f = LivestockFilter(self.request.GET, queryset=Livestock.objects.filter(active=True))
        return f.qs


class LivestockCreateView(BSModalCreateView):
    template_name = 'livestock/create_livestock.html'
    form_class = LivestockModelForm
    success_message = 'Ganado creado exitosamente.'
    success_url = reverse_lazy('livestocks')

    def post(self, request, *args, **kwargs):
        response = super(LivestockCreateView,self).post(request, *args, **kwargs)
        if self.object.id:
            LivestockWeightHistory.objects.create(
                    livestock_id = self.object,
                    weight = float(request.POST['weight_current'])
                )
            if request.POST['weight_current'] != request.POST['weight_initial']:
                initial = LivestockWeightHistory.objects.create(
                    livestock_id = self.object,
                    date_record = request.POST['optional_date'],
                    weight = float(request.POST['weight_initial'])
                )
        return response


class LivestockUpdateView(BSModalUpdateView):
    model = Livestock
    template_name = 'livestock/update_livestock.html'
    form_class = LivestockUpdateModelForm
    success_message = 'Ganado actualizado exitosamente.'
    success_url = reverse_lazy('livestocks')

    def post(self, request, *args, **kwargs):
        response = super(LivestockUpdateView,self).post(request, *args, **kwargs)
        if float(request.POST['weight_current']) != self.get_object().weight_current:
            LivestockWeightHistory.objects.create(
                livestock_id = self.get_object(),
                weight = float(request.POST['weight_current'])
            )
        return response


class LivestockDeleteView(BSModalDeleteView):
    model = Livestock
    template_name = 'livestock/delete_livestock.html'
    success_message = 'ganado eliminado correctamente'
    success_url = reverse_lazy('livestocks')

    def post(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.active = False
        self.object.save()
        return HttpResponseRedirect(success_url)


class LivestockFilterView(BSModalFormView):
    template_name = 'livestock/filter_livestock.html'
    form_class = LivestockFilterForm

    def form_valid(self, form):
        if 'clear' in self.request.POST:
            self.filter = ''
        else:
            self.filter = ''
            for k in self.request.POST.keys():
                if k=='csrfmiddlewaretoken':
                    continue
                elif self.request.POST[k] != '':
                    self.filter += ('?' if self.filter == '' else '&') + k + '=' + (str(form.cleaned_data[k].id) if k.endswith('_id') else str(form.cleaned_data[k]) )
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('livestocks') + self.filter

# Income Views

class IncomeListView(generic.ListView):
    model = Income
    context_object_name = 'incomes'
    template_name = 'income/incomes.html'
    paginate_by = 5

    def get_queryset(self):
        f = IncomeFilter(self.request.GET, queryset=Income.objects.filter(active=True))
        return f.qs


class IncomeCreateView(BSModalCreateView):
    template_name = 'income/create_income.html'
    form_class = IncomeModelForm
    success_message = 'Ingreso creado exitosamente.'
    success_url = reverse_lazy('incomes')

    def post(self, request, *args, **kwargs):
        response = super(IncomeCreateView,self).post(request, *args, **kwargs)
        if self.object.id:
            self.object.product_id.onhand_qty = self.object.product_id.onhand_qty + self.object.quantity
            self.object.product_id.save()
        return response


class IncomeDeleteView(BSModalDeleteView):
    model = Income
    template_name = 'income/delete_income.html'
    success_message = 'Ingreso eliminado correctamente'
    success_url = reverse_lazy('incomes')

    def post(self, request, *args, **kwargs):
        response = super(IncomeDeleteView,self).post(request, *args, **kwargs)
        if self.object:
            self.object.product_id.onhand_qty = self.object.product_id.onhand_qty - self.object.quantity
            self.object.product_id.save()
        return response


class IncomeFilterView(BSModalFormView):
    template_name = 'income/filter_income.html'
    form_class = IncomeFilterForm

    def form_valid(self, form):
        if 'clear' in self.request.POST:
            self.filter = ''
        else:
            self.filter = ''
            for k in self.request.POST.keys():
                if k=='csrfmiddlewaretoken':
                    continue
                elif self.request.POST[k] != '':
                    self.filter += ('?' if self.filter == '' else '&') + k + '=' + (str(form.cleaned_data[k].id) if k.endswith('_id') else str(form.cleaned_data[k]) )
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('incomes') + self.filter

    
# Outcome Views

class OutcomeListView(generic.ListView):
    model = Outcome
    context_object_name = 'outcomes'
    template_name = 'outcome/outcomes.html'
    paginate_by = 5

    def get_queryset(self):
        f = OutcomeFilter(self.request.GET, queryset=Outcome.objects.filter(active=True))
        return f.qs


class OutcomeCreateView(BSModalCreateView):
    template_name = 'outcome/create_outcome.html'
    form_class = OutcomeModelForm
    success_message = 'Ingreso creado exitosamente.'
    success_url = reverse_lazy('outcomes')

    def post(self, request, *args, **kwargs):
        response = super(OutcomeCreateView,self).post(request, *args, **kwargs)
        if self.object.id:
            self.object.product_id.onhand_qty = self.object.product_id.onhand_qty - self.object.quantity
            self.object.product_id.save()
        return response


class OutcomeDeleteView(BSModalDeleteView):
    model = Outcome
    template_name = 'outcome/delete_outcome.html'
    success_message = 'Ingreso eliminado correctamente'
    success_url = reverse_lazy('outcomes')

    def post(self, request, *args, **kwargs):
        response = super(OutcomeDeleteView,self).post(request, *args, **kwargs)
        if self.object:
            self.object.product_id.onhand_qty = self.object.product_id.onhand_qty + self.object.quantity
            self.object.product_id.save()
        return response


class OutcomeFilterView(BSModalFormView):
    template_name = 'outcome/filter_outcome.html'
    form_class = OutcomeFilterForm

    def form_valid(self, form):
        if 'clear' in self.request.POST:
            self.filter = ''
        else:
            self.filter = ''
            for k in self.request.POST.keys():
                if k=='csrfmiddlewaretoken':
                    continue
                elif self.request.POST[k] != '':
                    self.filter += ('?' if self.filter == '' else '&') + k + '=' + (str(form.cleaned_data[k].id) if k.endswith('_id') else str(form.cleaned_data[k]) )
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('outcomes') + self.filter