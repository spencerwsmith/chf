__author__ = 'Spencer'
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission, ContentType


class Users(AbstractUser):
    #password
    #last_login
    #is_superuser boolean
    #username
    #first_name
    #last_name
    #email
    #is_staff boolean
    #is_active boolean
    #date_joined
    #objects
    address1 = models.TextField(max_length=90)
    address2 = models.TextField(max_length=50)
    city = models.TextField(max_length=30)
    state = models.TextField(max_length=2)
    zip = models.TextField(max_length=13)
    security_question = models.TextField(null=True, blank=True)
    security_answer = models.TextField(null=True, blank=True)
    reset_code = models.TextField(null=True, blank=True)
    exp_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username


class Agent(Users):
    appointmentDate = models.DateField(blank=True, null=True)
    emergency_contact = models.TextField(max_length=100, blank=True, null=True)
    emergency_phone = models.TextField(max_length=15, blank=True, null=True)
    emergency_relation = models.TextField(max_length=30, blank=True, null=True)
    bio_sketch = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.username


class Session(models.Model):
    expire_date = models.DateField(blank=True, null=True)
    session_date = models.DateField(blank=True, null=True)
    users = models.ForeignKey(Users, null=True, blank=True, related_name='+')

    def __str__(self):
        return self.expire_date


class Shopping_Cart(models.Model):
    session = models.OneToOneField(Session, blank=True, null=True)

    def __str__(self):
        return self.session


class Product(models.Model):
    name = models.TextField(max_length=30, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    description = models.TextField(max_length=200, blank=True, null=True)
    manufacturer = models.TextField(max_length=200, blank=True, null=True)
    average_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sku = models.TextField(max_length=200, blank=True, null=True)
    order_form_name = models.TextField(max_length=200, blank=True, null=True)
    production_time = models.TextField(max_length=200, blank=True, null=True)
    category = models.TextField(max_length=30, blank=True, null=True)
    isrental = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Stocked_Product(Product):
    quantity_on_hand = models.TextField(max_length=10, blank=False, null=False)
    order_field = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Cart_Line_Item(models.Model):
    quantity = models.IntegerField()
    stocked_product = models.ForeignKey(Stocked_Product, related_name='+', blank=True, null=True)

    def __str__(self):
        return self.stocked_product


class Serialized_Product(Stocked_Product):
    serial_number = models.TextField(max_length=200, blank=False, null=False)
    date_acquired = models.DateField(blank=True, null=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
    status = models.TextField(max_length=200, blank=True, null=True)
    for_sale = models.BooleanField(default=False)
    condition_new = models.TextField(max_length=200, blank=True, null=True)
    notes = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.serial_number

class WardrobeItem(Serialized_Product):
    size = models.TextField(max_length=15, blank=False, null=False)
    size_modifier = models.TextField(max_length=30, blank=True, null=True)
    gender = models.TextField(max_length=10, blank=False, null=False)
    color = models.TextField(max_length=30, blank=True, null=True)
    pattern = models.TextField(max_length=30, blank=True, null=True)
    start_year = models.TextField(max_length=4, blank=True, null=True)
    end_year = models.TextField(max_length=4, blank=True, null=True)

    def __str__(self):
        return self.serial_number


class Transaction(models.Model):
    customer = models.ForeignKey(Users, related_name='+', blank=False, null=False)
    date = models.DateTimeField()
    phone = models.TextField(max_length=12, blank=True, null=True)
    date_packed = models.DateTimeField(blank=True, null=True)
    date_shipped = models.DateTimeField(blank=True, null=True)
    packed_by = models.ForeignKey(Agent, related_name='+', blank=True, null=True)
    shipped_by = models.ForeignKey(Agent, related_name='+', blank=True, null=True)
    tracking_number = models.TextField(max_length=35, blank=True, null=True)

    def __str__(self):
        return self.tracking_number


class Line_Item(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transaction = models.ForeignKey(Transaction, related_name='+', blank=True, null=True)

    def __str__(self):
        return self.transaction


class Sale_Item(Line_Item):
    quantity = models.IntegerField()
    product = models.ForeignKey(Stocked_Product, blank=True, null=True)

    def __str__(self):
        return self.transaction


class Rental_Product(WardrobeItem):
    is_wardrobe_item = models.BooleanField(default=False)
    times_rented = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    replacement_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name


class Rented_Item(Line_Item):
    date_out = models.DateField(blank=True, null=True)
    date_due = models.DateField(blank=True, null=True)
    date_in = models.DateField(blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    rental_product = models.ForeignKey(Rental_Product, related_name='+', blank=True, null=True)
    renter = models.ForeignKey(Users, blank=True, null=True)

    def __str__(self):
        return self.amount


class Fee(Line_Item):
    waived = models.BooleanField(default=False)
    rented_item = models.ForeignKey(Rented_Item, related_name='+', blank=True, null=True)

    def __str__(self):
        return self.transaction


class Late_Fee(Fee):
    days_late = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.transaction


class Damage_Fee(Fee):
    description = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.transaction


class Event(models.Model):
    name = models.TextField(max_length=100, blank=False, null=False)
    type = models.TextField(max_length=100, blank=False, null=False)
    location = models.TextField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    address1 = models.TextField(max_length=100, blank=True, null=True)
    address2 = models.TextField(max_length=100, blank=True, null=True)
    city = models.TextField(max_length=100, blank=True, null=True)
    state = models.TextField(max_length=100, blank=True, null=True)
    zip = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Area(models.Model):
    aname = models.TextField(max_length=50)
    description = models.TextField(max_length=500, blank=True, null=True)
    coordinator = models.ForeignKey(Agent, related_name='+', blank=True, null=True)
    supervisor = models.ForeignKey(Agent, related_name='+', blank=True, null=True)
    event = models.ForeignKey(Event, blank=True, null=True)

    def __str__(self):
        return self.aname


class Expected_Sale_Item(models.Model):
    name = models.TextField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=100, blank=False, null=False)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    area = models.ForeignKey(Area, related_name='+', blank=True, null=True)

    def __str__(self):
        return self.name


class Historical_Figure(models.Model):
    name = models.TextField(max_length=100, blank=False, null=False)
    birthdate = models.DateField(blank=True, null=True)
    birthplace = models.TextField(max_length=100, blank=True, null=True)
    deathdate = models.DateField(blank=True, null=True)
    is_functional = models.BooleanField(default=False)
    bio = models.TextField(max_length=600, blank=True, null=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.TextField(max_length=100, blank=False, null=False)
    type = models.TextField(max_length=50, blank=True, null=True)
    historical_figure = models.ForeignKey(Historical_Figure, blank=True, null=True)

    def __str__(self):
        return self.name
