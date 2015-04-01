__author__ = 'Spencer'
from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.models import Group, Permission, ContentType
import random
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group

templater = get_renderer('homepage')

########################################################################################################################
#View Event


@view_function
def process_request(request):
    params = {}

    params['events'] = hmod.Event.objects.all()

    return templater.render_to_response(request, 'events.html', params)

########################################################################################################################
#Create Event

@view_function
@permission_required('homepage.add_event')
def create(request):
    '''Creates a new event'''
    event = hmod.Event()
    event.name = ''
    event.start_date = '2012-02-20'
    event.end_date = '2012-02-20'
    event.location = ''
    event.save()

    return HttpResponseRedirect('/homepage/events.edit/{}/'.format(event.id))

########################################################################################################################
#Edit Event

@view_function
@permission_required('homepage.change_event')
def edit(request):
    params = {}

    try:
        event = hmod.Event.objects.get(id=request.urlparams[0])
    except hmod.Event.DoesNotExist:
        return HttpResponseRedirect('/homepage/events/')

    form = EventEditForm(initial={
        'name': event.name,
        'startDate': event.start_date,
        'endDate': event.end_date,
        'location': event.location,
    })
    if request.method == 'POST':
        form = EventEditForm(request.POST)
        form.eventid = event.id
        if form.is_valid():
            event.name = form.cleaned_data['name']
            event.start_date = form.cleaned_data['startDate']
            event.end_date = form.cleaned_data['endDate']
            event.location = form.cleaned_data['location']
            event.save()
            return HttpResponseRedirect('/homepage/events/')

    params['form'] = form
    params['event'] = event
    return templater.render_to_response(request, 'events.edit.html', params)


class EventEditForm(forms.Form):
    name = forms.CharField(label="Event Name", required=True, max_length=80)
    start_date = forms.DateField(label="Start Date", required=True)
    end_date = forms.DateField(label="End Date", required=True)
    location = forms.CharField(label="Location Name", required=True, max_length=80)

    '''def clean_username(self):
        if len(self.cleaned_data['username']) < 5:
            raise forms.ValidationError("Please enter a username with at least 5 characters")

        user_count = hmod.Users.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if user_count >= 1:
            raise forms.ValidationError("Sorry, but that username is already taken")

        return self.cleaned_data['username']'''


########################################################################################################################
#Delete Event

@view_function
@permission_required('homepage.delete_event')
def delete(request):
    try:
        event = hmod.Event.objects.get(id=request.urlparams[0])
    except hmod.Event.DoesNotExist:
        return HttpResponseRedirect('/homepage/events/')

    event.delete()
    return HttpResponseRedirect('/homepage/events/')