from django.contrib import admin
from .models import Products, ProductsCategory

# Register your models here.

class ProductsCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    search_fields = ('name',)
    list_display=('name', 'created', 'updated')
    ordering = ('-created',)
    
class ProductsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    search_fields = ('name', 'cost', 'fLote')
    list_display=('name', 'amount', 'cost', 'category', 'created', 'updated')
    ordering = ('-created',)
    
admin.site.register(ProductsCategory, ProductsCategoryAdmin)
admin.site.register(Products, ProductsCategoryAdmin)
