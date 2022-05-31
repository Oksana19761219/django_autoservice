from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Model, Car, Service, Order, OrderLine
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q

class OrderListView(generic.ListView):
    model = Order
    paginate_by = 2
    template_name = 'orders.html'
    context_object_name = 'orders'


def index(request):
    service_count = Service.objects.all().count()
    order_count = Order.objects.all().count()
    order_finished_count = Order.objects.filter(status__exact='i').count()
    car_count = Car.objects.all().count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'service_count': service_count,
        'order_count': order_count,
        'order_finished_count': order_finished_count,
        'car_count': car_count,
        'num_visits': num_visits,
    }


    return render(request, 'index.html', context=context)


def cars(request):
    paginator = Paginator(Car.objects.all(), 3)
    page_number = request.GET.get('page')
    paged_cars = paginator.get_page(page_number)
    context = {'cars': paged_cars}
    return render(request, 'cars.html', context=context)


def car(request, car_id):
    single_car = get_object_or_404(Car, pk=car_id)
    return render(request, 'car.html', {'car': single_car})


def search(request):

    query = request.GET.get('query')
    search_results = Car.objects.filter(
        Q(client__icontains=query) |
        Q(number__icontains=query) |
        Q(vin_number__icontains=query)
    )
    return render(request, 'search.html', {'cars': search_results, 'query': query})