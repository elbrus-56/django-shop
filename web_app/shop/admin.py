from django.contrib import admin
from .models import *




class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'price', 'image')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Products, ProductsAdmin)
