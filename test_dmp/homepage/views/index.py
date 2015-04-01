__author__ = 'Spencer'
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django import forms
from .. import dmp_render, dmp_render_to_response
from django.contrib.auth import authenticate, login
from datetime import datetime
import random
from django.core.mail import send_mail
import random
import homepage.models as hmod


@view_function
def process_request(request):
    template_vars = {}

    return dmp_render_to_response(request, 'index.html', template_vars)


@view_function
def loginform(request):
    template_vars = {}

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponse('''
             <script>
              window.location.href = '/homepage/index';
             </script>
              ''')

    template_vars['form'] = form
    return dmp_render_to_response(request, 'index.loginform.html', template_vars)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user == None:
            raise forms.ValidationError("Sorry, that's not right")
        return self.cleaned_data






