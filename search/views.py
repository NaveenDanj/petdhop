from django.shortcuts import render , redirect
from product.models import *
from API.getter import *
# Create your views here.

def search_page(request):

    if request.method == 'GET':

        if request.user.is_authenticated:

            if request.GET.get('query'):
                
                try:
                    q = request.GET.get('query')
                    cat = request.GET.get('category')

                    ret_data = []

                    
                    products = Product.objects.filter(name__icontains = q )

                    if cat == 'all':
                        ret_data = []

                        for p in products:

                            thmb = Product_Image.objects.filter(product_id = p)[0]
                            ret_data.append({"data" : p , 'thumb' : thmb})


                    else:

                        c_obj = Category.objects.get(category_id = cat)

                        for p in products:

                            if Product_Category.objects.filter(product_id = p , cat_id = c_obj ).count() > 0:
                                thmb = Product_Image.objects.filter(product_id = p)[0]
                                ret_data.append({"data" : p , 'thumb' : thmb , 'ratings' : get_customer_full_review(p.pid)})


                    obj = {'num_array' : [1,2,3,4,5] , "products" : ret_data , "len" : len(ret_data) , "q" : request.GET.get('query') , "all_cats" : get_all_categories() , 'cart_data' : get_cart_data(request.user)[0] , 'total_price' : get_cart_data(request.user)[1] , 'all_items' : len(get_cart_data(request.user)[0])  }


                    return render(request , 'search_page.html' , obj)
                except Exception as e:
                    return redirect('')

            else:
                return render(request , '404.html')

        else:
            return redirect('/login')
    else:
        return render(request , '404.html')
