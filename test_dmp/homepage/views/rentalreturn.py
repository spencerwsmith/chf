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


@view_function
def process_request(request):
    template_vars = {}

    form = rrform()
    if request.method == 'POST':
        form = rrform(request.POST)
        if form.is_valid():
            renter = hmod.Users.objects.get(renter=form.cleaned_data['username'])
            sku = form.cleaned_data['reset_code']
            date_in = form.cleaned_data['date_in']



    template_vars['form'] = form
    return dmp_render_to_response(request, 'passcode.html', template_vars)


class rrform(forms.Form):
    renter = forms.ChoiceField(hmod.Users.objects.all())
    sku = forms.CharField()
    date_in = forms.DateField()

