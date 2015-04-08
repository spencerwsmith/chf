__author__ = 'Spencer'
from django.conf import settings
from django import forms
from .. import dmp_render, dmp_render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django.contrib.auth import authenticate, login
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import random
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission, ContentType
from django.core.mail import send_mail
import random
import requests
import datetime



@view_function
def process_request(request):
    template_vars = {}

    rentalsout = hmod.Rented_Item.objects.filter(date_in__isnull=True)
    template_vars['rentalsout'] = rentalsout


    form = rrform(initial={
        'renter': Rented_Item.renter,
        'rentalid': hmod.Rented_Item.rentalid,
        'product_name': hmod.Rented_Item.product_name,
        'sku': hmod.Rented_Item.sku,
        'date_in': datetime.date.today(),
        'damages': '',
        'description': ''
    })

    if request.method == 'POST':
        form = rrform(request.POST)
        if form.is_valid():
            API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
            API_KEY = '29b716033cf11e06afd6bdf91c6b38ed'
            print(form.cleaned_data['renter'])
            user = hmod.Users.objects.get(username=form.cleaned_data['renter'])

            renter = form.cleaned_data['renter']
            rentalid = form.cleaned_data['rentalid']
            product_name = form.cleaned_data['product_name']
            sku = form.cleaned_data['sku']
            date_in = form.cleaned_data['date_in']
            damages = form.cleaned_data['damages']
            description = form.cleaned_data['description']

            Rented_Item = hmod.Rented_Item.objects.get(rentalid=form.cleaned_data['rentalid'])
            Rented_Item.date_in = form.cleaned_data['date_in']
            Rented_Item.save()
            print(Rented_Item.rentalid)
            print(Rented_Item.date_in)


            r = requests.post(API_URL, data={
                'apiKey': API_KEY,
                'currency': 'usd',
                'amount': damages,
                'type': form.cleaned_data['type'],
                'number': form.cleaned_data['number'],
                'exp_month': form.cleaned_data['exp_month'],
                'exp_year': form.cleaned_data['exp_year'],
                'cvc': form.cleaned_data['cvc'],
                'name': 'Cosmo Limesandal',
                'description': 'Charge for cosmo@is411.byu.edu'
            })

            template_vars['amount'] = damages
            template_vars['description'] = description
            template_vars['product_name'] = product_name
            print(r.text)

            resp = r.json()
            if 'error' in resp:
                print("ERROR: ", resp['error'])
                return dmp_render_to_response(request, 'ccerror.html', template_vars)

            else:
                print(resp.keys())
                print(resp['ID'])

            body = dmp_render(request, 'damages.html', template_vars)

            send_mail('CHF Receipt', body, 'spencerw.smith@yahoo.com',
            [user.email], fail_silently=False, html_message=body)



            template_vars['form'] = form
            return dmp_render_to_response(request, 'rrprocessed.html', template_vars)



    template_vars['form'] = form
    return dmp_render_to_response(request, 'rentalreturn.html', template_vars)


#allGroups = Users.groups.all()
'''groups = forms.ModelMultipleChoiceField(queryset=groupChoice)'''
Card_Choices = (
    (Visa, "Visa"),
    (MasterCard, "MasterCard"),
    (Amex, "Amex")
)

template_vars = {}
cardtypes = {'Visa', 'MasterCard', 'Amex'}
template_vars['cards'] = ['Visa', 'MasterCard', 'Amex']
allUsers = hmod.Users.objects.all()
allProducts = hmod.Rental_Product.objects.all()
class rrform(forms.Form):
    renter = forms.CharField(label="Renter's Username")
    rentalid = forms.CharField(label="Rental ID")
    product_name = forms.CharField(label="Product Name")
    sku = forms.CharField()
    date_in = forms.DateField(label='Date In (MM/DD/YY)')
    damages = forms.CharField(label="Damages Charge")
    description = forms.CharField(label="Description of Damages")
    type = models.CharField(choices=Card_Choices, label="Card Type")
    number = forms.CharField(label="Credit Card ggggNumber", max_length=16, min_length=10)
    exp_month = forms.CharField(max_length=2, min_length=2)
    exp_year = forms.CharField(max_length=2, min_length=2)
    cvc = forms.CharField(max_length=4, label="CVC", min_length=3)

