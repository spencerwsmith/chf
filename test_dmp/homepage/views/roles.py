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
from django.contrib.auth.models import Group

templater = get_renderer('homepage')

########################################################################################################################
#View Role

@view_function
def process_request(request):
    params = {}

    params['roles'] = hmod.Role.objects.all()

    return templater.render_to_response(request, 'roles.html', params)

########################################################################################################################
#Create Role

@view_function
@permission_required('homepage.add_role')
def create(request):
    '''Creates a new role'''
    role = hmod.Role()
    role.name = ''
    role.type = ''
    role.save()

    return HttpResponseRedirect('/homepage/roles.edit/{}/'.format(role.id))

########################################################################################################################
#Edit Role

@view_function
@permission_required('homepage.change_role')
def edit(request):
    params = {}

    try:
        role = hmod.Role.objects.get(id=request.urlparams[0])
    except hmod.Role.DoesNotExist:
        return HttpResponseRedirect('/homepage/roles/')

    form = RoleEditForm(initial={
        'name': role.name,
        'type': role.type,
    })
    if request.method == 'POST':
        form = RoleEditForm(request.POST)
        form.roleid = role.id
        if form.is_valid():
            role.name = form.cleaned_data['name']
            role.type = form.cleaned_data['type']
            role.save()
            return HttpResponseRedirect('/homepage/roles/')

    params['form'] = form
    params['role'] = role
    return templater.render_to_response(request, 'roles.edit.html', params)


class RoleEditForm(forms.Form):
    name = forms.CharField(label="Role", required=True, max_length=80)
    type = forms.CharField(label="Type", required=True, max_length=80)


    '''def clean_username(self):
        if len(self.cleaned_data['username']) < 5:
            raise forms.ValidationError("Please enter a username with at least 5 characters")

        user_count = hmod.Users.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if user_count >= 1:
            raise forms.ValidationError("Sorry, but that username is already taken")

        return self.cleaned_data['username']'''


########################################################################################################################
#Delete Role

@view_function
@permission_required('homepage.delete_role')
def delete(request):
    try:
        role = hmod.Role.objects.get(id=request.urlparams[0])
    except hmod.Role.DoesNotExist:
        return HttpResponseRedirect('/homepage/roles/')

    role.delete()
    return HttpResponseRedirect('/homepage/roles/')