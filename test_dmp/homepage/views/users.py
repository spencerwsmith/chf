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
#
########################################################################################################################
# View Users


@view_function
@permission_required('homepage.change_users')
def process_request(request):
    params = {}

    params['users'] = hmod.Users.objects.all().order_by('username')

    return templater.render_to_response(request, 'users.html', params)


########################################################################################################################
#Create User

@view_function
@permission_required('homepage.add_users')
def create(request):
    '''Creates a new user'''
    user = hmod.Users.objects.create_user(
        username="Enter User Name Here",
        password="",
        first_name="",
        last_name="",
        email="",
        address1="",
        address2="",
        city="",
        state="",
        zip="",
        security_question="",
        security_answer=""
        )

    return HttpResponseRedirect('/homepage/users.edit/{}/'.format(user.id))


########################################################################################################################
#Edit User

@view_function
@permission_required('homepage.change_users')
def edit(request):

    params = {}

    try:
        user = hmod.Users.objects.get(id=request.urlparams[0])
    except hmod.Users.DoesNotExist:
        return HttpResponseRedirect('/homepage/users/')

    form = UserEditForm(initial={
        'username': user.username,
        'password': user.password,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'address1': user.address1,
        'address2': user.address2,
        'city': user.city,
        'state': user.state,
        'zip': user.zip,
        'security_question': user.security_question,
        'security_answer': user.security_answer
    })
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        Users = hmod.Users()
        form.userid = user.id
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.address1 = form.cleaned_data['address1']
            user.address2 = form.cleaned_data['address2']
            user.city = form.cleaned_data['city']
            user.state = form.cleaned_data['state']
            user.zip = form.cleaned_data['zip']
            user.security_question = form.cleaned_data['security_question']
            user.security_answer = form.cleaned_data['security_answer']
            user.save()
            '''groupSet = form.cleaned_data['groups']
            allGroups = Users.groups.all()

            ###Adds user to groups
            if groupSet:
                for group in groupSet:
                    try:
                        oGroup = Group.objects.get(id=group.id)
                        oGroup.user_set.add(user)
                    except Group.DoesNotExist:
                        'This group does not exist'

             ###Deletes user from groups
            for group in allGroups:
                if group not in groupSet:
                    group.user_set.remove(user)'''

            return HttpResponseRedirect('/homepage/users/')

    params['form'] = form
    params['user'] = user
    return templater.render_to_response(request, 'users.edit.html', params)


class UserEditForm(forms.Form):
    groupChoice = Group.objects.all()
    username = forms.CharField(label="User Name", required=True, max_length=80)
    password = forms.CharField(label="Password", required=True, max_length=80, widget=forms.PasswordInput)
    first_name = forms.CharField(label="First Name", required=True, max_length=80)
    last_name = forms.CharField(label="Last Name", required=True, max_length=80)
    email = forms.EmailField(required=True, max_length=80)
    address1 = forms.CharField(label="Address Line 1", required=True, max_length=150)
    address2 = forms.CharField(label="Address Line 2", required=False, max_length=80)
    city = forms.CharField(label="City", required=True, max_length=80)
    state = forms.CharField(label="St", required=True, max_length=40)
    zip = forms.CharField(label="ZIP Code", required=True, max_length=10)
    security_question = forms.CharField(label="Security Question", required=True, max_length=80)
    security_answer = forms.CharField(label="Security Answer", required=True, max_length=80)
    '''groups = forms.ModelMultipleChoiceField(queryset=groupChoice)'''

    def clean_username(self):
        if len(self.cleaned_data['username']) < 5:
            raise forms.ValidationError("Please enter a username with at least 5 characters")

        user_count = hmod.Users.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if user_count >= 1:
            raise forms.ValidationError("Sorry, but that username is already taken")

        return self.cleaned_data['username']


########################################################################################################################
#Delete User

@view_function
@permission_required('homepage.delete_users')
def delete(request):
    try:
        user = hmod.Users.objects.get(id=request.urlparams[0])
    except hmod.Users.DoesNotExist:
        return HttpResponseRedirect('/homepage/users/')

    user.delete()
    return HttpResponseRedirect('/homepage/users/')