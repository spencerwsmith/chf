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


@view_function
def process_request(request):
    template_vars = {}

    form = forgotpassform()
    if request.method == 'POST':
        form = forgotpassform(request.POST)
        if form.is_valid():
            user = hmod.Users.objects.get(username=form.cleaned_data['username'])

            # send the email
            ran = random.randint(1000, 100000000)
            exp_date = datetime.date.today() + datetime.timedelta(days=1)

            # reset password
            user.reset_code = ran
            user.exp_date = exp_date
            user.save()
            print(user.exp_date)

            template_vars['user'] = user
            body = dmp_render(request, 'pass.html', template_vars)

            send_mail('New CHF Password Code', body, 'spencerw.smith@yahoo.com',
            [user.email], fail_silently=False, html_message=body)

            # httpresponseredirect to a different url that says "check your email"
            return dmp_render_to_response(request, 'email_forgot_password.html', template_vars)

    template_vars['form'] = form
    return dmp_render_to_response(request, 'forgotpassword.html', template_vars)


class forgotpassform(forms.Form):
    username = forms.CharField()

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'))

        return self.cleaned_data
