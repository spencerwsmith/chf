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
            renter = form.cleaned_data['renter']
            sku = form.cleaned_data['sku']
            date_in = form.cleaned_data['date_in']
            damages = form.cleaned_data['damages']
            description = form.cleaned_data['description']

            template_vars['form'] = form
            return dmp_render_to_response(request, 'rrprocessed.html', template_vars)



    template_vars['form'] = form
    return dmp_render_to_response(request, 'rentalreturn.html', template_vars)


#allGroups = Users.groups.all()
'''groups = forms.ModelMultipleChoiceField(queryset=groupChoice)'''
allUsers = hmod.Users.objects.all()
class rrform(forms.Form):
    renter = forms.ModelMultipleChoiceField(queryset=allUsers)
    sku = forms.CharField()
    date_in = forms.DateField(label='Date In (MM/DD/YY)')
    damages = forms.CharField()
    description = forms.CharField()

