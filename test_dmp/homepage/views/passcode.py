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
import datetime


@view_function
def process_request(request):
    template_vars = {}

    form = passcodeform()
    if request.method == 'POST':
        form = passcodeform(request.POST)
        if form.is_valid():
            user = hmod.Users.objects.get(username=form.cleaned_data['username'])
            reset_code = form.cleaned_data['reset_code']

            #ds = datetime.date.today() - Rented_Item.date_due
            rd = datetime.date.today() - user.exp_date
            rt = abs(rd.days)
            print(rd)
            print(rt)

            if reset_code == user.reset_code and rt >= 0:

                template_vars['user'] = user
                #return dmp_render_to_response(request, '/homepage/myaccountpass/${ user.id }/', template_vars)
                return dmp_render_to_response(request, 'myaccount.html', template_vars)
            else:
                #All this code would need to be in the clean statement raise forms.ValidationError("Sorry, that is not a valid entry")
                return dmp_render_to_response(request, 'error.html', template_vars)


    template_vars['form'] = form
    return dmp_render_to_response(request, 'passcode.html', template_vars)


class passcodeform(forms.Form):
    username = forms.CharField()
    reset_code = forms.CharField()

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'))

        return self.cleaned_data
