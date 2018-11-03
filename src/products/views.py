from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Product

class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = "products/featured-detail.html"


class ProductListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

class ProductDetailView(DetailView):
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get("pk")
        return Product.objects.filter(pk=pk)

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get("pk")
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product does not exist")
        return instance

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get("slug")
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found.")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Oh oh")
        return instance







