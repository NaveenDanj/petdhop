from django.shortcuts import render , redirect
from account.models import Account
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from checkout.models import Order , Order_Product
from API.getter import *

# Create your views here.


def acoount_page(request):

    if request.user.is_authenticated:

        try:
            user_obj = Account.objects.filter(user_id = request.user)[0]
            
            order_data = Order.objects.filter(user_id = request.user)

            all_orders = []


            for i in range(len(order_data)-1 , -1 , -1 ):

                all_orders.append(order_data[i])

            all_products = []

            for item in order_data:

                products = Order_Product.objects.filter(order_id = item)

                all_products.append(products)

            

            data_obj = {"all_cats" : get_all_categories() , "user_data" : user_obj , "order_data" : all_orders , 'cart_data' : get_cart_data(request.user)[0] , 'all_items' : len(get_cart_data(request.user)[0]) , 'total_price' : get_cart_data(request.user)[1]}


            return render(request , 'account.html' , data_obj)
            
        except :

            return render(request , '404.html')

    else:
        return redirect('/login')



def update_account(request):

    if request.user.is_authenticated:
        if request.method == 'POST':
            
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            address = request.POST.get('address')
            mobile = request.POST.get('mobile')
            town = request.POST.get('town')
            state = request.POST.get('state')
            zipcode = request.POST.get('zipcode')


            if len(fname) == 0 or len(lname) == 0 or len(address) == 0 or len(mobile) == 0 or len(town) == 0 or len(state) == 0 or len(zipcode) == 0 :
                return render(request , '404.html')
            else:

                if len(fname) < 6 or len(lname) < 6 or len(address) < 15 or len(mobile) < 10:
                    return render(request , '404.html')
                else:
                    
                    try:

                        obj = Account.objects.get(user_id = request.user)
                        obj.fname = fname
                        obj.lname = lname
                        obj.address = address
                        obj.mobile_number = mobile
                        obj.town = town
                        obj.state = state
                        obj.zipcode = zipcode
                        obj.save()

                        c_password = request.POST.get('current_password')
                        new_password = request.POST.get('new_password')
                        comfirm_password = request.POST.get('comfirm_password')

                        if c_password != '' and new_password != '' and comfirm_password != '':

                            if request.user.check_password(c_password) :

                                if new_password == comfirm_password:
                                    saveuser = User.objects.get(id= request.user.id)
                                    saveuser.set_password(new_password)
                                    saveuser.save()

                                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                                else:
                                    messages.info(request , "Password not match!")
                                    return redirect('/account')

                            else:
                                messages.info(request , "Current Password is incorrect!")
                                return redirect('/account')
                        else:
                            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


                    except:

                        return render(request , '404.html')

        else:
            return render(request , '404.html')

    else:
        return redirect('/')



            






            

