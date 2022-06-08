from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import User
from django.views import generic
from django.views.generic.edit import FormMixin
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import OrderReviewForm
from .models import Model, Car, Service, Order, OrderLine
from django.utils.translation import gettext as _


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


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if not password or password == password2:
            if not username or User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                if not email or User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')


class OrdersView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'my_orders.html'
    paginate_by = 10

    def get_queryset(self):
        print(self.request.user)
        print(Order.objects.filter(car_id__client_id=self.request.user))
        return Order.objects.filter(car_id__client_id=self.request.user)






# class OrderDetailView(FormMixin, generic.DetailView):
#     model = Order
#     template_name = 'order_detail.html'
#     form_class = OrderReviewForm
#
#     class Meta:
#         ordering = ['data']
#
#     def get_success_url(self):
#         return reverse('order_detail', kwargs={'pk': self.object.id})
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#     def form_valid(self, form):
#         form.instance.order_id = self.object
#         form.instance.reviewer = self.request.user
#         form.save()
#         return super(OrderDetailView, self).form_valid(form)
