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
    params = {

    }

    user = hmod.Users.objects.get(id=request.urlparams[0])

    ran = random.randint(1000, 100000000)

    send_mail('New CHF Password', 'Your new password is: %s' % ran, 'spencerw.smith@yahoo.com',
        [user.email], fail_silently=False)

    return dmp_render_to_response(request, 'forgotpassword.html', params)