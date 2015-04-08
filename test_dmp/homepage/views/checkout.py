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
import datetime
import random
import requests
import getpass


@view_function
def process_request(request):
    template_vars = {}
    try:
        user = hmod.Users.objects.get(id=request.urlparams[0])
        print(str(user.username))
    except hmod.Users.DoesNotExist:
        return HttpResponseRedirect('/homepage/index/')
    '''try:
        user = getpass.getuser()       #hmod.Users.objects.get(id=request.urlparams[0])
        print(str(user.username))
    except hmod.Users.DoesNotExist:
        return HttpResponseRedirect('/homepage/index/')'''

    form = checkoutform(initial={
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'address1': user.address1,
        'address2': user.address2,
        'city': user.city,
        'state': user.state,
        'zip': user.zip,
        'amount': '',
        'type': '',
        'number': '',
        'exp_month': '',
        'exp_year': '',
        'cvc': ''

    })

    if request.method == 'POST':
        form = checkoutform(request.POST)
        if form.is_valid():
            API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
            API_KEY = '29b716033cf11e06afd6bdf91c6b38ed'
            user = hmod.Users.objects.get(username=form.cleaned_data['username'])

            #reset_code = form.cleaned_data['reset_code']
            # do form.cleaned data, instead of hard coding it in
            r = requests.post(API_URL, data={
                'apiKey': API_KEY,
                'currency': 'usd',
                'amount': '5.99',
                'username': form.cleaned_data['username'],
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'address1': form.cleaned_data['address1'],
                'address2': form.cleaned_data['address2'],
                'city': form.cleaned_data['city'],
                'state': form.cleaned_data['state'],
                'zip': form.cleaned_data['zip'],
                'type': form.cleaned_data['type'],
                'number': form.cleaned_data['number'],
                'exp_month': form.cleaned_data['exp_month'],
                'exp_year': form.cleaned_data['exp_year'],
                'cvc': form.cleaned_data['cvc'],
                'name': 'Cosmo Limesandal',
                'description': 'Charge for cosmo@is411.byu.edu'
            })

            print(r.text)

            resp = r.json()
            if 'error' in resp:
                print("ERROR: ", resp['error'])

            else:
                print(resp.keys())
                print(resp['ID'])

            send_mail('CHF Receipt', 'Thank you for your purchase', 'spencerw.smith@yahoo.com',
            [user.email], fail_silently=False)




            return dmp_render_to_response(request, 'purchase.html', template_vars)

    template_vars['form'] = form
    return dmp_render_to_response(request, 'checkout.html', template_vars)



class checkoutform(forms.Form):
    username = forms.CharField(label="User Name")
    first_name = forms.CharField(label="First Name", max_length=55)
    last_name = forms.CharField(label="Last Name", max_length=55)
    address1 = forms.CharField(label="Address Line 1", max_length=80)
    address2 = forms.CharField(label="Address Line 2", max_length=80)
    city = forms.CharField(label="City", max_length=40)
    state = forms.CharField(label="St", max_length=14)
    zip = forms.CharField(label="ZIP", max_length=11)
    #currency = 'usd'
    amount = '3.99' #get this from session?
    type = forms.CharField(label="Card Type")
    number = forms.CharField(label="Credit Card Number", max_length=16)
    exp_month = forms.CharField(max_length=2)
    exp_year = forms.CharField(max_length=2)
    cvc = forms.CharField(max_length=4, label="CVC")
    #name = 'Cosmo Limesandal'
    #description = 'Charge for cosmo@is411.byu.edu'

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'))

        return self.cleaned_data