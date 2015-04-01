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



@view_function
def process_request(request):
    template_vars = {}

    form = forgotpassform()
    if request.method == 'POST':
        form = forgotpassform(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'])
        pass
    pass

    template_vars['form'] = form
    return dmp_render_to_response(request, 'forgotpassword.html', template_vars)


class forgotpassform(forms.Form):
    username = forms.CharField()
    email = forms.CharField()

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'))

        return self.cleaned_data
