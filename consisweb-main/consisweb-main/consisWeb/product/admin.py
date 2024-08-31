from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_name', 'entry_date', 'update_date', 'status')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'stock', 'entry_date', 'update_date', 'status', 'category')
    list_filter = ('category', 'status')
    search_fields = ('product_name',)
