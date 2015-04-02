__author__ = 'Spencer'
from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
#import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import random
from django.contrib.auth.decorators import permission_required
from .. import dmp_render, dmp_render_to_response
import datetime
from django.core.mail import send_mail
import requests


@view_function
def process_request(request):
    params = {}

    API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
    API_KEY = '29b716033cf11e06afd6bdf91c6b38ed'

    r = requests.post(API_URL, data={
        'apiKey': API_KEY,
        'currency': 'usd',
        'amount': '5.99',
        'type': 'Visa',
        'number': '4732817300654',
        'exp_month': '10',
        'exp_year': '15',
        'cvc': '411',
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


    return dmp_render_to_response(request, 'purchase.html', params)