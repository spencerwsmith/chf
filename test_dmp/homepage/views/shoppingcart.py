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
from datetime import date
import random
import requests, getpass

@view_function
def process_request(request):
    params = []

    user = request.user
    print(str(user.username))
    print(str(user.id))

    rows = []
    cart = request.session["shopping_cart"]
    for key, qty in cart.items():
        product = hmod.Product.objects.get(id=key)
        price = product.price * qty
        name = product.name

        if product.isrental is not True:
            rows.append('''
            <div class='cart-item'>
                <b><div style="color:green">Purchase:</div></b>
                <div class="cart-left">%s</div>
                <div class='cart-middle'>Quantity: <input class='product-quantity' name="%s" type='number' required max='200' min='1' value='%d'/></div>
                <div class="cart-right">
                    <span class="glyphicon glyphicon-usd" aria-hidden="true"></span> %s
                    <a href ="/homepage/shoppingcart.remove?id=%s"><button class="btn btn-danger">Remove</button></a>

                    </a>

                </div>
                <br>
            </div>
            ''' % (name, key, qty, "{:,}".format(price), key))
        else:
            rows.append('''
            <div class='cart-item'>
                <b><div style="color:green">Rental:</div></b>
                <div class="cart-left">%s</div>
                <div class='cart-middle'>Days: <input class='product-quantity' name="%s" type='number' required max='200' min='1' value='%d'/></div>
                <div class="cart-right">
                    <span class="glyphicon glyphicon-usd" aria-hidden="true"></span> %s
                    <a href ="/homepage/shoppingcart.remove?id=%s"><button class="btn btn-danger">Remove</button></a>

                    </a>

                </div>
                <br>
            </div>
            ''' % (name, key, qty, "{:,}".format(price), key))
    rows.append('''<div align='right'><a href="/homepage/shoppingcart.checkout/%d/"class="btn btn-warning">Checkout</a></div> ''' % user.id)
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
    days = request.urlparams[2]
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

    print('before try except')

    try:
        print('before user =')
        user = hmod.Users.objects.get(id=request.urlparams[0])
        print('after get user')
    except hmod.Users.DoesNotExist:
        return HttpResponseRedirect('/homepage/users/')

    form = checkoutform(initial={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'address1': user.address1,
        'address2': user.address2,
        'city': user.city,
        'state': user.state,
        'zip': user.zip


    })

    if request.method == 'POST':
        form = checkoutform(request.POST)
        if form.is_valid():
            API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
            API_KEY = '29b716033cf11e06afd6bdf91c6b38ed'
            #user = hmod.Users.objects.get(username=form.cleaned_data['username'])

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

                allrentals = hmod.Rented_Item.objects.all()
                allrentals.count()
                allrentals2 = allrentals.count()
                print(allrentals2)


                ds = datetime.date.today() + datetime.timedelta(1*365/12)

                print(ds)



                if product.isrental is not False:
                    rental_product = hmod.Rental_Product.objects.get(name=product.name)
                    rented_item = hmod.Rented_Item()
                    rented_item.renter = user
                    rented_item.rentalid = (allrentals2 + 1)
                    rented_item.rental_product = rental_product
                    rented_item.amount = product.price
                    rented_item.date_out = datetime.date.today()
                    rented_item.date_due = ds
                    rented_item.date_in = None
                    rented_item.save()


            #for loop to take out each product in productlist
            template_vars['tp'] = totalprice

            # do form.cleaned data, instead of hard coding it in
            r = requests.post(API_URL, data={
                'apiKey': API_KEY,
                'currency': 'usd',
                'amount': '5.99',
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'address1': form.cleaned_data['address1'],
                'address2': form.cleaned_data['address2'],
                'city': form.cleaned_data['city'],
                'state': form.cleaned_data['state'],
                'zip': form.cleaned_data['zip'],
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

            request.session['shopping_cart'] = {}

            body = dmp_render(request, 'email_receipt.html', template_vars)

            send_mail('CHF Receipt', body, 'spencerw.smith@yahoo.com',
            [user.email], fail_silently=False, html_message=body)

            #If it is a rental then make the due date todays date

            return dmp_render_to_response(request, 'purchase.html', template_vars)

    template_vars['form'] = form
    return dmp_render_to_response(request, 'checkout.html', template_vars)


Card_Choices = (
    ('Visa', "Visa"),
    ('MasterCard', "MasterCard"),
    ('Amex', "Amex")
)
class checkoutform(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=55)
    last_name = forms.CharField(label="Last Name", max_length=55)
    address1 = forms.CharField(label="Address Line 1", max_length=80)
    address2 = forms.CharField(label="Address Line 2", max_length=80, required=False)
    city = forms.CharField(label="City", max_length=40)
    state = forms.CharField(label="St", max_length=14)
    zip = forms.CharField(label="ZIP", max_length=11)
    #currency = 'usd'
    #amount = forms.CharField() #get this from session?
    type = forms.MultipleChoiceField(choices=Card_Choices, label="Credit Type")
    number = forms.CharField(label="Credit Card Number", max_length=16, min_length=10)
    exp_month = forms.CharField(max_length=2, min_length=2)
    exp_year = forms.CharField(max_length=2, min_length=2)
    cvc = forms.CharField(max_length=4, label="CVC", min_length=3)
    #name = 'Cosmo Limesandal'
    #description = 'Charge for cosmo@is411.byu.edu'

    def clean(self):
        #user = authenticate(username=self.cleaned_data.get('username'))

        return self.cleaned_data


