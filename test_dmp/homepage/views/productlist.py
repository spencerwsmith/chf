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

    catalog_items = hmod.Product.objects.all()

    template_vars['catalog_items'] = catalog_items
    return dmp_render_to_response(request, 'productlist.html', template_vars)