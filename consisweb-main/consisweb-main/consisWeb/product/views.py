from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, Product

# List views
class CategoryListView(ListView):
    model = Category
    template_name = 'product/category_list.html'

class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'

# Detail views
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'product/category_detail.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

# Create views
class CategoryCreateView(CreateView):
    model = Category
    template_name = 'product/category_form.html'
    fields = ['cat_name', 'status']

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/product_form.html'
    fields = ['product_name', 'image', 'status', 'price', 'stock', 'category']

# Update views
class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'product/category_form.html'
    fields = ['cat_name', 'status']

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/product_form.html'
    fields = ['product_name', 'image', 'status', 'price', 'stock', 'category']

# Delete views
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'product/category_confirm_delete.html'
    success_url = reverse_lazy('category-list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')
