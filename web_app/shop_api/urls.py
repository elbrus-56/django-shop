from django.urls import path
from shop_api.views import ProductAPIView

urlpatterns = [
    path('api/v1/products/', ProductAPIView.as_view()),

]