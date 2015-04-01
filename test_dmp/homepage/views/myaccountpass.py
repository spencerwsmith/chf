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
from django.contrib.auth.models import Group, Permission, ContentType

from django.shortcuts import redirect

templater = get_renderer('homepage')


########################################################################################################################
#Edit Account Password

@view_function
def process_request(request):

    params = {}

    try:
        user = hmod.Users.objects.get(id=request.urlparams[0])
    except hmod.Users.DoesNotExist:
        return HttpResponseRedirect('/homepage/index/')


    form = PasswordForm(initial={
        'username': user.username,
        'password': user.password,
    })
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        user = hmod.Users()
        form.userid = user.id
        user = hmod.Users.objects.get(id=request.urlparams[0])
        user.delete()
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.save()

            return HttpResponseRedirect('/homepage/index/')

    params['form'] = form
    params['user'] = user
    return templater.render_to_response(request, 'myaccount.editpass.html', params)


class PasswordForm(forms.Form):
    groupChoice = Group.objects.all()
    username = forms.CharField(label="User Name", required=True, max_length=80)
    password = forms.CharField(label="New Password", required=True, max_length=80, widget=forms.PasswordInput)

    def clean_username(self):
        if len(self.cleaned_data['username']) < 5:
            raise forms.ValidationError("Please enter a username with at least 5 characters")

        user_count = hmod.Users.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if user_count >= 1:
            raise forms.ValidationError("Sorry, but that username is already taken")

        return self.cleaned_data['username']






