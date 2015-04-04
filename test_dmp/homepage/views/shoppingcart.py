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
from django.core.mail import send_mail
import datetime
import random
import requests

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


@view_function
def checkout(request):
    template_vars = {}

    form = checkoutform()
    if request.method == 'POST':
        form = checkoutform(request.POST)
        if form.is_valid():
            API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
            API_KEY = '29b716033cf11e06afd6bdf91c6b38ed'
            user = hmod.Users.objects.get(username=form.cleaned_data['username'])

            #Get shopping cart info to get total price and send receipt
            cart = request.session["shopping_cart"]
            print(str(cart))

            template_vars['productlist'] = []
            template_vars['pricelist'] = []
            totalprice = 0

            for key, qty in cart.items():
                product = hmod.Product.objects.get(id=key)
                price = product.price * qty
                totalprice = totalprice + price
                name = product.name
                print(name)
                print(price)
                template_vars['productlist'].append([name, price])
                template_vars['pricelist'].append(price)

            #for loop to take out each product in productlist
            template_vars['tp'] = totalprice

            # do form.cleaned data, instead of hard coding it in
            r = requests.post(API_URL, data={
                'apiKey': API_KEY,
                'currency': 'usd',
                'amount': totalprice,
                'type': form.cleaned_data['type'],
                'number': form.cleaned_data['number'],
                'exp_month': form.cleaned_data['exp_month'],
                'exp_year': form.cleaned_data['exp_year'],
                'cvc': form.cleaned_data['cvc'],
                'name': 'Cosmo Limesandal',
                'description': 'Charge for cosmo@is411.byu.edu'
            })

            print(r.text)

            resp = r.json()
            if 'error' in resp:
                print("ERROR: ", resp['error'])

            else:
                print(resp.keys())
                print(resp['ID'])

            body = dmp_render(request, 'email_receipt.html', template_vars)

            send_mail('CHF Receipt', body, 'spencerw.smith@yahoo.com',
            [user.email], fail_silently=False, html_message=body)

            #If it is a rental then make the due date todays date




            return dmp_render_to_response(request, 'purchase.html', template_vars)

    template_vars['form'] = form
    return dmp_render_to_response(request, 'checkout.html', template_vars)


class checkoutform(forms.Form):
    username = forms.CharField()
    #currency = 'usd'
    #amount = forms.CharField() #get this from session?
    type = forms.CharField(label="Card Type")
    number = forms.CharField(label="Credit Card Number", max_length=16, min_length=10)
    exp_month = forms.CharField(max_length=2, min_length=2)
    exp_year = forms.CharField(max_length=2, min_length=2)
    cvc = forms.CharField(max_length=4, label="CVC", min_length=3)
    #name = 'Cosmo Limesandal'
    #description = 'Charge for cosmo@is411.byu.edu'

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'))

        return self.cleaned_data



