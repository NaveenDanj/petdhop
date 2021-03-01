from django.shortcuts import render , redirect
from product.models import Product
from cart.models import Cart
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from API.getter import *
# Create your views here.

def add_to_cart(request):
    
    if request.method == 'POST':
        if request.user.is_authenticated :

            amount = request.POST.get('amount')
            pid = request.POST.get('pid')

            p = Product.objects.filter(pid = pid)[0]

            if len(Cart.objects.filter(user_id = request.user , product_id = p)) == 0:
                total = int(amount) * p.new_price
                Cart.objects.create(user_id = request.user , product_id = p , amount = amount , total = total )
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                cart_obj = Cart.objects.filter(user_id = request.user , product_id = p)[0]
                try:
                    cart_obj.amount += int(amount)
                    cart_obj.total = cart_obj.amount * cart_obj.product_id.new_price
                    cart_obj.save()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                except Exception as e:
                    return render(request , '404.html')
                
            return redirect('/')
        else:
            return redirect('/login')
    else:
        return render(request , '404.html')


def cart_page(request):

    if request.user.is_authenticated :

        try :
            user_cart = Cart.objects.filter(user_id = request.user)

            sub_total = 0

            for i in range(len(user_cart)):
                sub_total = sub_total + user_cart[i].total
            
            data = {"all_cats" : get_all_categories() , "cart_" : user_cart , "cart_items_length" : len(user_cart) , "sub_total" : sub_total ,'cart_data' : get_cart_data(request.user)[0] , 'total_price' : get_cart_data(request.user)[1] , 'all_items' : len(get_cart_data(request.user)[0])}

            return render(request , 'cart.html' , data)

        except Exception as e:
            return render(request , '404.html')


        return render(request , 'cart.html')


def update_cart(request):

    if request.method == 'POST':
        if request.user.is_authenticated :

            amount = request.POST.get('amount')
            pid = request.POST.get('product_id')

            p = Product.objects.filter(pid = pid)[0]
            
            try:
                cart_obj = Cart.objects.filter(user_id = request.user , product_id = p)[0]

                if int(amount) == 0:
                    Cart.objects.filter(user_id = request.user , product_id = p).delete()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                cart_obj.amount = int(amount)
                cart_obj.total = cart_obj.amount * cart_obj.product_id.new_price
                cart_obj.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            except Exception as e:
                return render(request , '404.html')

        else:
            return redirect('/login')

    else:
        return render(request , '404.html')


def reset_cart(request):
    if request.method == 'POST':
        if request.user.is_authenticated :
            try:
                Cart.objects.filter(user_id = request.user).delete()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            except Exception as e:
                return render(request , '404.html')

        else:
            return redirect('/login')

    else:
        return render(request , '404.html')



def del_cart_item(request):
    
    if request.method == 'POST':
        if request.user.is_authenticated :

            cart_id = request.POST.get('cart_id')

            try :
                obj = Cart.objects.filter(id = cart_id)[0]
                obj.delete()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except Exception as e:
                return render(request , '404.html')

        else:
            return redirect('/login')

    else:
        return render(request , '404.html')
