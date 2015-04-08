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
from .. import dmp_render, dmp_render_to_response


@view_function
def process_request(request):
    template_vars = {}

    '''product = hmod.Product.objects.get(id=1)
    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}
        if product.id not in request.session['shopping_cart']:
            request.session['shopping_cart'][product.id] = 1
        else:
            request.session['shopping_cart'][product.id] += 1'''

    catalog_items = hmod.Product.objects.filter(isrental=False)
    rentals = hmod.Rental_Product.objects.all()

    template_vars['rentals'] = rentals
    template_vars['catalog_items'] = catalog_items
    return dmp_render_to_response(request, 'productcatalog.html', template_vars)