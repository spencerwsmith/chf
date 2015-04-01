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

templater = get_renderer('homepage')

########################################################################################################################
#View Agent

@view_function
def process_request(request):
    params = {}

    params['agents'] = hmod.Agent.objects.all().order_by('last_name')

    return templater.render_to_response(request, 'agents.html', params)

########################################################################################################################
#Create Agent

@view_function
@permission_required('homepage.add_agent')
def create(request):
    '''Creates a new agent'''
    agent = hmod.Agent(
        username='',
        password='',
        first_name='',
        last_name='',
        email='',
        last_login='2014-02-20 00:00:00-07',
        is_superuser='False',
        is_active='True',
        is_staff='False',
        date_joined='2014-02-20 00:00:00-07',
        address1='',
        address2='',
        city='',
        state='',
        zip='',
        security_question='',
        security_answer='',
        appointmentDate="2012-02-20"
        )
    agent.save()

    return HttpResponseRedirect('/homepage/agents.edit/{}/'.format(agent.id))

########################################################################################################################
#Edit Agent

@view_function
@permission_required('homepage.change_agent')
def edit(request):
    params = {}

    try:
        agent = hmod.Agent.objects.get(id=request.urlparams[0])
    except hmod.Agent.DoesNotExist:
        return HttpResponseRedirect('/homepage/agents/')

    form = AgentEditForm(initial={
        'username': agent.username,
        'password': agent.password,
        'first_name': agent.first_name,
        'last_name': agent.last_name,
        'email': agent.email,
        'address1': agent.address1,
        'address2': agent.address2,
        'city': agent.city,
        'state': agent.state,
        'zip': agent.zip,
        'security_question': agent.security_question,
        'security_answer': agent.security_answer,
        'appointmentDate': agent.appointmentDate
        })

    if request.method == 'POST':
        form = AgentEditForm(request.POST)
        form.agentid = agent.id
        if form.is_valid():
            agent.username = form.cleaned_data['username']
            agent.set_password(form.cleaned_data['password'])
            agent.first_name = form.cleaned_data['first_name']
            agent.last_name = form.cleaned_data['last_name']
            agent.email = form.cleaned_data['email']
            agent.address1 = form.cleaned_data['address1']
            agent.address2 = form.cleaned_data['address2']
            agent.city = form.cleaned_data['city']
            agent.state = form.cleaned_data['state']
            agent.zip = form.cleaned_data['zip']
            agent.security_question = form.cleaned_data['security_question']
            agent.security_answer = form.cleaned_data['security_answer']
            agent.appointmentDate = form.cleaned_data['appointmentDate']
            agent.save()
            return HttpResponseRedirect('/homepage/agents/')

    params['form'] = form
    params['agent'] = agent
    return templater.render_to_response(request, 'agents.edit.html', params)


class AgentEditForm(forms.Form):
    username = forms.CharField(label="User Name", required=True, max_length=80)
    password = forms.CharField(label="Password", required=True, max_length=80)
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
    appointmentDate = forms.DateField(label="Appointment Date", required=True)

    def clean_username(self):
        if len(self.cleaned_data['username']) < 5:
            raise forms.ValidationError("Please enter a username with at least 5 characters")

        user_count = hmod.Users.objects.filter(username=self.cleaned_data['username']).exclude(id=self.agentid).count()
        if user_count >= 1:
            raise forms.ValidationError("Sorry, but that username is already taken")

        return self.cleaned_data['username']


########################################################################################################################
#Delete Agent

@view_function
@permission_required('homepage.delete_agent')
def delete(request):
    try:
        agent = hmod.Agent.objects.get(id=request.urlparams[0])
    except hmod.Agent.DoesNotExist:
        return HttpResponseRedirect('/homepage/agents/')

    agent.delete()
    return HttpResponseRedirect('/homepage/agents/')