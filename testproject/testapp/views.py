# myapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Customer

# دالة لعرض الصفحة الرئيسية
def index(request):
    return render(request, 'index.html')

# دالة لعرض بيانات الزبائن في صيغة JSON
def customer_list(request):
    customers = Customer.objects.all()
    customer_data = list(customers.values())  # تحويل البيانات إلى قائمة من القواميس
    return JsonResponse(customer_data, safe=False)


def get_products(request):
    products = Product.objects.all()
    product_data = list(products.values('id', 'name', 'price', 'description'))
    return JsonResponse(product_data, safe=False)