from django.db import models
from django.urls import reverse


class Model(models.Model):
    car_brand = models.CharField(
        'car brand',
        max_length=100,
        null=False,
        help_text='Enter car brand (for example, Toyota)'
    )
    car_model = models.CharField(
        'car model',
        max_length=100,
        null=False,
        help_text='Enter car model (for example, Corolla)'
    )
    year = models.IntegerField(
        'year',
        null=True,
        help_text='Enter car production year'
    )

    def __str__(self):
        return f'{self.car_brand} {self.car_model}, {self.year}'

    def get_absolute_url(self):
        return reverse('model-detail', args=[str(self.id)])

    class Meta:
        ordering = ['car_brand', 'car_model', 'year']
        verbose_name = 'Model'
        verbose_name_plural = 'Models'



class Car(models.Model):
    number = models.CharField(
        'number',
        max_length=10,
        null=False,
        help_text='Enter car number'
    )
    model_id = models.ForeignKey(
        Model,
        on_delete=models.CASCADE,
        null=False,
        verbose_name='Model',
        related_name='cars'
    )
    vin_number = models.CharField(
        'VIN number',
        max_length=17,
        null=False,
        help_text='17 symbols <a href="https://www.autodna.com/vin-number">VIN number</a>'
    )
    client = models.CharField(
        'client',
        max_length=250,
        null=False,
        help_text='Enter client name'
    )

    def __str__(self):
        return f'{self.number}, {self.model_id}'

    def get_absolute_url(self):
        return reverse('car-detail', args=[str(self.id)])

    class Meta:
        ordering = ['number']
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'



class Service(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='Service name'
    )
    price = models.FloatField(
        'price',
        null=False,
        help_text='service price'
    )

    def __str__(self):
        return f'{self.name}, {self.price}'

    class Meta:
        ordering = ['name']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'



class Order(models.Model):
    data = models.DateField(
        'order data',
        null=False,
        blank=False
    )
    car_id = models.ForeignKey(
        Car,
        null=False,
        on_delete=models.CASCADE,
        verbose_name='Car',
        related_name='orders'
    )

    LOAN_STATUS = (
        ('l', 'Laukia'),
        ('v', 'Vykdoma'),
        ('i', 'įvykdyta'),
        ('a', 'atšaukta'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='l',
        help_text='Status',
    )

    def __str__(self):
        return f'{self.car_id}, {self.data}'

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])

    class Meta:
        ordering = ['car_id', 'data']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderLine(models.Model):
    order_id = models.ForeignKey(
        Order,
        null=False,
        on_delete=models.CASCADE,
        verbose_name='order',
        related_name='orders_lines'
    )
    quantity = models.IntegerField(
        'quantity',
        null=False,
        help_text='service quantity'
    )
    service_id = models.ForeignKey(
        Service,
        null=False,
        on_delete=models.CASCADE,
        verbose_name='service',
        related_name='orders_lines'
    )
    def __str__(self):
        return f'{self.order_id}, {self.service_id}, {self.quantity}'

    def get_absolute_url(self):
        return reverse('order-line-detail', args=[str(self.id)])