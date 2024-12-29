# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # صفحة العرض الرئيسية
    path('api/customers/', views.customer_list, name='customer_list'),  # API لعرض الزبائن
    path('api/products/', views.get_products, name='product_list'),

]
