from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name='cars'),
    path('cars/<int:car_id>', views.car, name='car'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('order_detail/', views.register, name='order_detail'),
    path('my_orders/', views.OrdersView.as_view(), name='my_orders'),
    path('i18n/', include('django.conf.urls.i18n')),
]
