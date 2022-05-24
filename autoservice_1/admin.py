from django.contrib import admin
from .models import Model, Car, Service, Order, OrderLine


class ModelAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'car_model', 'year')
    list_filter = ('car_brand', 'year')

class OrderInline(admin.TabularInline):
    model = Order
    extra = 0 # išjungia placeholder'ius

class CarAdmin(admin.ModelAdmin):
    list_display = ('model_id', 'number', 'vin_number', 'client')
    list_filter = ('client', 'model_id')
    search_fields = ('client', 'number')
    inlines = [OrderInline]

class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 0 # išjungia placeholder'ius

class OrderAdmin(admin.ModelAdmin):
    list_display = ('data', 'car_id', 'status')
    list_filter = ('data', 'car_id')
    search_fields = ('car_id__number',)
    inlines = [OrderLineInline]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')



admin.site.register(Model, ModelAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(OrderLine)
