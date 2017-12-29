from django.shortcuts import render
from django.http import HttpResponse
from .models import Order

def index(request):
    return HttpResponse("hello")

def user_order(request, tracking_id):
    user_orders = Order.objects.filter(order=Order.objects.filter(tracking_id=tracking_id))
    return render(request, 'order/user_order.html', {'user_orders': user_orders})
