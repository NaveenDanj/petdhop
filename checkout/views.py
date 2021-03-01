from django.shortcuts import render , redirect
from cart.models import Cart
from django.http import HttpResponseRedirect
from account.models import Account
from cart.models import Cart
from uuid import uuid4
from checkout.models import Order , Order_Product
from product.models import Product
from django.http import HttpResponseRedirect
from dashboard.models import *


# Create your views here.


def gen_uuid() -> str:
    """Return a str representation of a uuid4"""
    return str(uuid4())




def checkout_page(request):

    if request.user.is_authenticated:

        user_cart = []
        acc = None

        try:
            user_cart = Cart.objects.filter(user_id = request.user)
            acc = Account.objects.filter(user_id = request.user)[0]

            print(acc)

        except Exception as e :

            print("the error is " , e)
            return render(request , '404.html')

        total = 0
        cart_len = len(user_cart)

        for item in user_cart:
            total += item.total

        orderid = gen_uuid()
        item_name = "PETMARK INVOICE"
        url_token = gen_uuid()

        obj = {"total" : total , "len" : cart_len , "account" : acc , "cart" : user_cart , "order_id" : orderid , "item_invoice" : item_name}

        if cart_len > 0:
            return render(request , 'checkout.html' , obj)
        else:
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            return render(request , '404.html')



def place_order(request):

    if request.method == "POST":

        if request.user.is_authenticated:

            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            address = request.POST.get('address')
            town = request.POST.get('town')
            state = request.POST.get('state')
            zipcode = request.POST.get('zipcode')
            coupon_code = request.POST.get('coupon_code')

            return redirect('/checkout')


def success_payment(request):

    if request.user.is_authenticated:

        user_account_id = request.GET.get('user_id')
        auth_id = request.user.username

        if user_account_id == auth_id:
            
            user_cart = Cart.objects.filter(user_id = request.user)

            order_total = 0

            for item in user_cart:
                order_total = order_total + item.total

            order = Order.objects.create(user_id = request.user , total = order_total)
            Notification.objects.create(notify_type = 'New Order' , notify_text = auth_id + " has has placed an new order")

            for item in user_cart:

                product_obj = Product.objects.get(pid = item.product_id.pid)

                Order_Product.objects.create( order_id = order , product_id = product_obj , amount = item.amount , total = item.total )

            Cart.objects.filter(user_id = request.user).delete()

            return redirect('/')

        else:

            return render(request , '404.html')

    else:

        return redirect('/login')
 

