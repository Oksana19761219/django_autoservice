from django.shortcuts import render
from django.http import HttpResponse
from .models import Model, Car, Service, Order, OrderLine

def index(request):
    service_count = Service.objects.all().count()
    order_count = Order.objects.all().count()
    order_finished_count = Order.objects.filter(status__exact='i').count()
    car_count = Car.objects.all().count()
    context = {
        'service_count': service_count,
        'order_count': order_count,
        'order_finished_count': order_finished_count,
        'car_count': car_count,
    }


    return render(request, 'index.html', context=context)
