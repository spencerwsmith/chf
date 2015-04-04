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
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, STRATEGY_ASYNC_THREADED, SEARCH_SCOPE_WHOLE_SUBTREE, GET_ALL_INFO




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

            username = form.cleaned_data['username'] #'Spencer@colheritagefoundation.local'
            pw = form.cleaned_data['password'] #'spencer24'

            try:
                s = Server('colheritagefoundation.info', port=8484, get_info=GET_ALL_INFO)

                c = Connection(s, auto_bind=True, client_strategy=STRATEGY_SYNC, user=username, password=pw, authentication=AUTH_SIMPLE, raise_exceptions=False)
                #
                print(c)
                print(c.user)

                if c is not None:
                    print('Ready to get or create a new user')
                    u, created = hmod.Users.objects.get_or_create(username=username)
                    print('got or created username')
                    #user_info = c.response[0]['attributes']
                    '''u.first_name = c.
                    u.last_name = c.
                    u.email = c.'''
                    u.set_password(pw)
                    u.save()
                    print('user received or created')

                    print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
                    u2 = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                    login(request, u2)
                    return HttpResponse('''
                    <script>
                    window.location.href = '/homepage/index';
                    </script>
                    ''')
                else:
                    print('something is broken')

            except:
                print('not going to c is not none')
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
        '''if user == None:
            raise forms.ValidationError("Sorry, that's not right")'''
        return self.cleaned_data






