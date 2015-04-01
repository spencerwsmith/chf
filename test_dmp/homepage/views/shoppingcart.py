__author__ = 'Spencer'
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django import forms
from .. import dmp_render, dmp_render_to_response
import homepage.models as hmod
from django.contrib.auth import authenticate, login
from datetime import datetime
import random


@view_function
def process_request(request):
    rows = []
    cart = request.session["shopping_cart"]
    for key, qty in cart.items():
        product = hmod.Product.objects.get(id=key)
        price = product.price * qty
        name = product.name
        rows.append('''
        <div class='cart-item'>
            <div class="cart-left">%s</div>
            <div class='cart-middle'>Quantity: <input class='product-quantity' name="%s" type='number' required max='200' min='1' value='%d'/></div>
            <div class="cart-right">
                <span class="glyphicon glyphicon-usd" aria-hidden="true"></span> %s
                <a href="/homepage/shoppingcart.remove?id=%s"><button class="btn btn-danger">Remove</button></a>
            </div>
        </div>
        ''' % (name, key, qty, "{:,}".format(price), key))
    html = "\n"
    html = html.join(rows)
    return HttpResponse(html)


@view_function
def add(request):

    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}
    cart = request.session["shopping_cart"]
    pid = request.urlparams[0]
    qty = request.urlparams[1]
    if pid in cart:
        cart[pid] += int(qty)
    else:
        cart[pid] = int(qty)

    request.session["shopping_cart"] = cart
    print(cart)

    return HttpResponseRedirect('/homepage/shoppingcart/')


@view_function
def delete(request):
    template_vars = []


@view_function
def update(request):
    if request.method != "POST":
        return HttpResponse(0)

    cart = request.session["shopping_cart"]
    for item, qty in dict(request.POST).items():
        quantity = int(qty[0])
        cart[item] = quantity
    request.session["shopping_cart"] = cart
    html = process_request(request)
    return HttpResponse(html)


@view_function
def remove(request):
    if request.method != "GET":
        return HttpResponse(0)

    cart = request.session["shopping_cart"]
    item = request.GET.get("id")

    if item in cart:
        cart.pop(item, None)
    request.session["shopping_cart"] = cart
    html = process_request(request)
    print(str(cart))
    return HttpResponseRedirect('/homepage/productcatalog/')


@view_function
def checkout(request):
    pass


@view_function
def addform(request):
    template_vars = {}

    form = AddForm()
    if request.method == 'POST':
        form = AddForm(request.POST)
        return HttpResponse('''
             <script>
              window.location.href = '/homepage/shoppingcart';
             </script>
              ''')

    template_vars['form'] = form
    return dmp_render_to_response(request, 'shoppingcart.addform.html', template_vars)


class AddForm(forms.Form):
    QTY = forms.CharField()



