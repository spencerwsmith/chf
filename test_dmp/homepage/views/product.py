__author__ = 'Spencer'
from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import random
from django.contrib.auth.decorators import permission_required
'''from django.contrib.auth.forms import '''

templater = get_renderer('homepage')

########################################################################################################################
#View Product

@view_function
def process_request(request):
    params = {}

    params['products'] = hmod.Product.objects.all()

    return templater.render_to_response(request, 'product.html', params)

########################################################################################################################
#Create Product

@view_function
@permission_required('homepage.add_product')
def create(request):
    '''Creates a new product'''
    item = hmod.Product()
    item.name = ''
    item.price = ''
    item.description = ''
    item.manufacturer = ''
    item.average_cost = '0.00'
    item.sku = ''
    item.order_form_name = ''
    item.production_time = ''
    item.category = ''
    item.save()

    return HttpResponseRedirect('/homepage/product.edit/{}/'.format(item.id))


########################################################################################################################
#Edit Item

@view_function
@permission_required('homepage.change_product')
def edit(request):
    params = {}

    try:
        product = hmod.Product.objects.get(id=request.urlparams[0])
    except hmod.Product.DoesNotExist:
        return HttpResponseRedirect('/homepage/product/')

    form = ProductEditForm(initial={
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'manufacturer': product.manufacturer,
        'average_cost': product.average_cost,
        'sku': product.sku,
        'order_form_name': product.order_form_name,
        'production_time': product.production_time,
        'category': product.category
    })
    if request.method == 'POST':
        form = ProductEditForm(request.POST)
        form.productid = product.id
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            product.manufacturer = form.cleaned_data['manufacturer']
            product.average_cost = form.cleaned_data['average_cost']
            product.sku = form.cleaned_data['sku']
            product.order_form_name = form.cleaned_data['order_form_name']
            product.production_time = form.cleaned_data['production_time']
            product.category = form.cleaned_data['category']
            product.save()
            return HttpResponseRedirect('/homepage/product/')

    params['form'] = form
    params['product'] = product
    return templater.render_to_response(request, 'product.edit.html', params)


class ProductEditForm(forms.Form):
    '''users = hmod.Users.objects.all()
    user = forms.ModelChoiceField(queryset=users)'''
    name = forms.CharField(label='Name', required=True, max_length=80)
    price = forms.DecimalField(label='Price', required=True)
    description = forms.CharField(label='Description', required=True, max_length=600)
    manufacturer = forms.CharField(label='Manufacturer', required=True, max_length=80)
    average_cost = forms.DecimalField(label='Average Cost', required=True)
    sku = forms.CharField(label='SKU', required=True, max_length=30)
    order_form_name = forms.CharField(label='Order Form Name', required=True, max_length=80)
    production_time = forms.CharField(label='Production Time', required=True, max_length=80)
    category = forms.CharField(label='Category', required=True, max_length=80)

    '''def clean_username(self):
        if len(self.cleaned_data['username']) < 5:
            raise forms.ValidationError("Please enter a username with at least 5 characters")

        user_count = hmod.Users.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if user_count >= 1:
            raise forms.ValidationError("Sorry, but that username is already taken")

        return self.cleaned_data['username']'''


########################################################################################################################
#Delete Product

@view_function
@permission_required('homepage.delete_item')
def delete(request):
    try:
        item = hmod.Product.objects.get(id=request.urlparams[0])
    except hmod.Product.DoesNotExist:
        return HttpResponseRedirect('/homepage/product/')

    item.delete()
    return HttpResponseRedirect('/homepage/product/')