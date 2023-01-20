from django.urls import path
from shop.views import *

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('catalog/', CatalogPage.as_view(), name='catalog'),
    path('catalog/<slug:cat_slug>/', CategoriesPage.as_view(), name='categories'),
    path('<slug:slug>', ProductDetail.as_view(), name='product_detail'),
    path('address/', address, name='address'),
    path('delivery/', delivery, name='delivery'),
    path('calc/', calc, name='calc'),
]
