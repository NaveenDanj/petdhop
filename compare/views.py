from django.shortcuts import render , redirect
from compare.models import Compare
from product.models import Product
from django.http import HttpResponseRedirect
from API.getter import *


# Create your views here.

def compare_page(request):

    if request.user.is_authenticated:
        if request.method == 'GET':
            try:
                objs = Compare.objects.filter(user_id = request.user)

                obj_data = []

                for item in objs:
                    img = Product_Image.objects.filter(product_id = item.product_id)[0]
                    cats = get_single_product(pidd =  item.product_id.pid)
                    obj_data.append({"data" : item ,  'image' : img , 'cats' : cats , 'ratings' : get_customer_full_review(item.product_id.pid)  })

                context = { "all_cats" : get_all_categories() , 'num_array' : [1,2,3,4,5] ,  "products" : obj_data , "len" : len(objs) , 'cart_data' : get_cart_data(request.user)[0] , 'total_price' : get_cart_data(request.user)[1] , 'all_items' : len(get_cart_data(request.user)[0])}
                return render(request , 'compare.html' , context)
            except Exception as e:
                return render(request , '404.html')

    return render(request , 'compare.html')


def add_compare(request):

    if request.method == 'POST':
        if request.user.is_authenticated:

            pid = request.POST.get('pid')
            user_id = request.user

            p = None

            try:
                p = Product.objects.filter(pid = pid)[0]
            except Exception as e:
                return render(request , '404.html')

            if len(Compare.objects.filter(user_id = request.user)) < 3 :
                if len(Compare.objects.filter(product_id = p )) == 0:

                    try:
                        p = Product.objects.filter(pid = pid)[0]
                        Compare.objects.create(user_id = user_id , product_id = p )
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                    except Exception as e:
                        return render(request , '404.html')

                else:
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                
        else:
            return redirect('/login')

    else:
        return render(request , '404.html')


def delete_compare(request):

    if request.method == 'POST':
        if request.user.is_authenticated :
            compare_id = request.POST.get('compare_id')
            try :
                obj = Compare.objects.filter(compare_id = compare_id)[0]
                obj.delete()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except Exception as e:
                return render(request , '404.html')

        else:
            return redirect('/login')

    else:
        return render(request , '404.html')