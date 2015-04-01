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
#View Sale Item


@view_function
def process_request(request):
    params = {}

    params['saleitems'] = hmod.SaleItem.objects.all()

    return templater.render_to_response(request, 'saleitems.html', params)


########################################################################################################################
#Create Sale Item

@view_function
@permission_required('homepage.add_saleitem')
def create(request):
    '''Creates a new sale item'''
    saleitem = hmod.SaleItem()
    saleitem.name = ''
    saleitem.description = ''
    saleitem.lowPrice = '0.00'
    saleitem.highPrice = '0.00'
    saleitem.area = ''
    saleitem.save()

    return HttpResponseRedirect('/homepage/saleitems.edit/{}/'.format(saleitem.id))

########################################################################################################################
#Edit Sale Item


@view_function
@permission_required('homepage.change_saleitem')
def edit(request):
    params = {}

    try:
        saleitem = hmod.SaleItem.objects.get(id=request.urlparams[0])
    except hmod.SaleItem.DoesNotExist:
        return HttpResponseRedirect('/homepage/saleitems/')

    form = SaleItemEditForm(initial={
        'name': saleitem.name,
        'description': saleitem.description,
        'lowPrice': saleitem.lowPrice,
        'highPrice': saleitem.highPrice,
        'area': saleitem.area,
    })
    if request.method == 'POST':
        form = SaleItemEditForm(request.POST)
        form.saleitemid = saleitem.id
        if form.is_valid():
            saleitem.name = form.cleaned_data['name']
            saleitem.description = form.cleaned_data['description']
            saleitem.lowPrice = form.cleaned_data['lowPrice']
            saleitem.highPrice = form.cleaned_data['highPrice']
            saleitem.area = form.cleaned_data['area']
            saleitem.save()
            return HttpResponseRedirect('/homepage/saleitems/')

    params['form'] = form
    params['saleitem'] = saleitem
    return templater.render_to_response(request, 'saleitems.edit.html', params)


class SaleItemEditForm(forms.Form):
    areas = hmod.Area.objects.all()
    name = forms.CharField(label="Name", required=True, max_length=80)
    description = forms.CharField(label="Description", required=True)
    lowPrice = forms.DecimalField(label="Low Price", required=True)
    highPrice = forms.DecimalField(label="High Price", required=True)
    area = forms.CharField(label="Area", required=False, max_length=40)

    '''def clean_username(self):
        if len(self.cleaned_data['username']) < 5:
            raise forms.ValidationError("Please enter a username with at least 5 characters")

        user_count = hmod.Users.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if user_count >= 1:
            raise forms.ValidationError("Sorry, but that username is already taken")

        return self.cleaned_data['username']'''


########################################################################################################################
#Delete Sale Item

@view_function
@permission_required('homepage.delete_saleitem')
def delete(request):
    try:
        saleitem = hmod.SaleItem.objects.get(id=request.urlparams[0])
    except hmod.SaleItem.DoesNotExist:
        return HttpResponseRedirect('/homepage/saleitems/')

    saleitem.delete()
    return HttpResponseRedirect('/homepage/saleitems/')