from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Model, Car, Service, Order, OrderLine
from django.views import generic

class OrderListView(generic.ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'orders'


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


def cars(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', {'cars': cars})

def car(request, car_id):
    single_car = get_object_or_404(Car, pk=car_id)
    return render(request, 'car.html', {'car': single_car})
