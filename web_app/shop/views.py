from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from shop.models import *

menu = [
    {'title': "Магазины", 'url_name': 'address'},
    {'title': "Доставка", 'url_name': 'delivery'},
    {'title': "Калькулятор", 'url_name': 'calc'}
]


class HomePage(TemplateView):

    template_name = 'shop/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Интернет-магазин SHOP - напольные покрытия в Челябинске '
        return context


class CatalogPage(ListView):
    model = Categories
    template_name = 'shop/category.html'
    context_object_name = 'categories'

    def get_context_data(self, object_list='None', *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Каталог напольных покрытий'
        context['products'] = Products.objects.all()
        return context


class CategoriesPage(CatalogPage):

    def get_context_data(self, *, object_list='None', **kwargs):
        context = super().get_context_data(**kwargs)
        query_from_categories = get_object_or_404(Categories, slug=self.kwargs['cat_slug'])
        context['title'] = query_from_categories.title
        context['menu'] = menu
        context['products'] = Products.objects.filter(category__slug=self.kwargs['cat_slug'])
        context['cat_selected'] = query_from_categories.id
        return context

    # def get_queryset(self):
    #     return Categories.objects.get(slug=self.kwargs['cat_slug'])


class ProductDetail(DetailView):

    model = Products

    template_name = 'shop/product.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['product'].title
        return context






def address(request):
    return HttpResponse("Адреса магазинов")


def delivery(request):
    return HttpResponse("Условия доставки")


def calc(request):
    return HttpResponse("Калькулятор")


# def product_detail(request, product_slug):
#     products_request = get_object_or_404(Products, slug=product_slug)

#     context = {
#         'menu': menu,
#         'product': products_request,
#         'title': products_request.title
#     }

#     return render(request, 'shop/product.html', context=context)
    # def get_queryset(self):
    #     return Products.objects.get(slug=self.kwargs['product_slug'])

# def request_all_from_categories():
#     return Categories.objects.all()


# def request_all_from_products():
#     return Products.objects.all()


# def index(request):
#     """
#     Функция, отвечающая за вывод главной страницы
#     """

#     context = {'title': 'Интернет-магазин напольных покрытий',
#                'menu': menu}

#     return render(request, 'shop/index.html', context=context)


# def catalog(request):
#     """
#     Функция, отвечающая за вывод страницы общего каталога
#     """

#     context = {'menu': menu,
#                'categories': request_all_from_categories(),
#                'products': request_all_from_products(),
#                'title': 'Каталог товаров'}

#     return render(request, 'shop/category.html', context=context)


# def categories(request, cat_slug):
#     """
#     Функция, отвечающая за вывод категорий товаров
#     """
#     categories_request = get_object_or_404(Categories, slug=cat_slug)
#     product_list = Products.objects.filter(category=categories_request.id)

#     context = {'cat_selected': cat_slug,
#                'menu': menu,
#                'categories': request_all_from_categories(),
#                'products': product_list,
#                'title': categories_request.title
#                }

#     return render(request, 'shop/category.html', context=context)
