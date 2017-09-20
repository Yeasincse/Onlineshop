from django.contrib import admin

# Register your models here.

from .models import Category, Product, Description_dises

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock','available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

class Description_disesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description',  'created', 'updated']
    list_filter = ['created', 'updated']
    list_editable = ['description']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Description_dises, Description_disesAdmin)