from django.shortcuts import render
from product.models import Product
from wishlist.models import Wishlist
from django.http import HttpResponseRedirect
from API.getter import *

# Create your views here.

def wishlist_page(request):

    if request.user.is_authenticated:

        wish_list = Wishlist.objects.filter(user_id = request.user)

        ret_data = []

        for item in wish_list:
            p = item.product_id
            thmb = Product_Image.objects.filter(product_id = p)[0]

            ret_data.append({'data' : item , 'thumb' : thmb })



        data = {"wish_list" : ret_data , "wishlist_len" : len(wish_list) , "all_cats" : get_all_categories()}

        return render(request , 'wishlist.html' , data )


def add_wish(request):

    if request.method == 'POST':
        if request.user.is_authenticated:

            product_id = request.POST.get('pid')
            obj = None

            try:
                obj = Product.objects.filter(pid = product_id)[0]

                if len(Wishlist.objects.filter(user_id = request.user , product_id = obj)) == 0:
                    Wishlist.objects.create(user_id = request.user , product_id = obj)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            except Exception as e:
                return render(request , '404.html')



def del_wish(request):

    if request.method == "POST":
        if request.user.is_authenticated:

            wish_id = request.POST.get('wid')
            product_id = request.POST.get('pid')
            obj = None

            try:
                obj = Wishlist.objects.filter(wish_id = wish_id)[0]
                obj.delete()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except Exception as e:
                return render(request , '404.html')

        else:
            return render(request , '404.html')

    else:
        return render(request , '404.html')

