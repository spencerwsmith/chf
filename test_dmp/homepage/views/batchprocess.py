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
from .. import dmp_render, dmp_render_to_response
import datetime
from django.core.mail import send_mail
from time import time


@view_function
def process_request(request):
    template_vars = {}

    overdueitems = hmod.Rented_Item.objects.filter(date_due__lt=datetime.date.today()).exclude(date_in__isnull=False)

    template_vars['sixty'] = []
    template_vars['thirty'] = []
    template_vars['zero'] = []

    for Rented_Item in overdueitems:
        ds = datetime.date.today() - Rented_Item.date_due
        dt = abs(ds.days)
        print(ds)
        print(dt)

        if dt >= 60:
            sixty = Rented_Item
            template_vars['sixty'].append(Rented_Item)
            print(Rented_Item.renter)

        elif dt < 60 & dt >= 30:
            thirty = Rented_Item
            template_vars['thirty'].append(Rented_Item)


        else:
            zero = Rented_Item
            template_vars['zero'].append(Rented_Item)



    template_vars['overdueitems'] = overdueitems



    return dmp_render_to_response(request, 'batchprocess.html', template_vars)


@view_function
def email(request):
    params = {

    }
    overdueitems = hmod.Rented_Item.objects.filter(date_due__lt=datetime.date.today()).exclude(date_in__isnull=False)

    for Rented_Item in overdueitems:
        ds = datetime.date.today() - Rented_Item.date_due
        dt = abs(ds.days)

        #email_body = dmp_render(request, 'You have an overdue item that you rented from the Colonial Heritage Foundation. It was due on', params)
        send_mail('Overdue Rental from CHF', 'You have an overdue item that you rented from CHF. The following product: %s was due on: %s and is now %s days overdue. Items can be returned at the CHF Headquarters. If you have any questions please contact Customer Support at 801-256-9087' % (Rented_Item.rental_product, Rented_Item.date_due, dt), 'spencerw.smith.byu@gmail.com',
            [Rented_Item.renter.email], fail_silently=False)

    return dmp_render_to_response(request, 'batchprocessemail.html', params)

































'''__author__ = 'Spencer'
from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import random
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission, ContentType

from django.shortcuts import redirect

templater = get_renderer('homepage')


    try:
        event = hmod.Event.objects.get(id=request.urlparams[0])
    except hmod.Event.DoesNotExist:
        return HttpResponseRedirect('/homepage/events/')



@view_function
def process_request(request):
    params = {}


class overdueForm(forms.Form):
    date_out = forms.DateField(label="Date Out")
    date_due = forms.DateField(label="Due Date")
    discount_percent = forms.CharField(label="Discount Percent")
    rental_product = forms.CharField(label="Rental Product")

    form = overdueForm(initial={
        'name': event.name,
        'startDate': event.start_date,
        'endDate': event.end_date,
        'location': event.location,
    })

    if request.method == 'POST':
        form = overdueForm(request.POST)

        return HttpResponseRedirect('/homepage/batchprocess/')


    params['rented items'] = hmod.Rented_Item.objects.all().order_by('date_due')
    params['overdueForm'] = form
    return templater.render_to_response(request, 'batchprocess.html', params)'''


