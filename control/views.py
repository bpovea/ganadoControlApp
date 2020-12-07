from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages

from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView, BSModalFormView
from bootstrap_modal_forms.mixins import DeleteMessageMixin

from .models import Product
from .forms import ProductModelForm,ProductUpdateModelForm,ProductFilterForm
from .filters import ProductFilter


def index(request):
    context = {'name':'Byron Povea'}
    return render(request,'index.html',context)


# Product Views

class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product/products.html'
    paginate_by = 20

    def get_queryset(self):
        f = ProductFilter(self.request.GET, queryset=Product.objects.all())
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
    success_message = 'Libro creado exitosamente.'
    success_url = reverse_lazy('products')


class ProductDeleteView(BSModalDeleteView):
    model = Product
    template_name = 'product/delete_product.html'
    success_message = 'Libro eliminado correctamente'
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
                    self.filter += ('?' if self.filter == '' else '&') + k + '=' + (str(form.cleaned_data[k].id) if k.endswith('_id') else form.cleaned_data[k] )
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('products') + self.filter