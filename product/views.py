from django.shortcuts import render , redirect
from product.models import Product , Comment
from datetime import date
from cart.models import Cart
from product.models import *
from API.getter import *

def product_details(request):

    if request.GET.get('pid') == None:
        return render( request , '404.html')
        
    else:

        data = []
        images = None
        img_thumb = None
        category_data = []

        product_id = request.GET.get('pid')

        try :
            data = Product.objects.filter(pid = product_id)
            images = Product_Image.objects.filter(product_id = data[0])
            img_thumb = images[0]

        except Exception as e :

            print("the error is " , e)

            return render(request , '404.html')

        if len(data) == 0:
            return render( request , '404.html')
        else:
            
            p_comments = []
            p_comments = Comment.objects.filter(pid = product_id)
            category_data = Product_Category.objects.filter(product_id = data[0])


            cart_data = Cart.objects.filter(user_id = request.user)

            total = 0

            for item in cart_data:

                total = total + item.product_id.new_price * item.amount


            all_cats = Category.objects.all()


            p_data = { 'avg_ratings' : get_customer_full_review(data[0]) , 'data' : data[0] , "all_cats" : get_all_categories() ,  "images" : images , "img_thumb" : img_thumb , 'p_comments' : p_comments , 'p_list' : [0,1,2,3,4] , 'all_comments' : len(p_comments) , 'cart_data' : get_cart_data(request.user)[0] , 'total_price' : total , 'all_items' : len(cart_data) , 'catss' : category_data , 'all_cats' : all_cats }

            return render(request , 'product_details.html' , p_data)



def add_comment(request):

    if request.method == 'POST':
        if request.user.is_authenticated :

            data = []

            ratings = request.POST.get('star')
            p_id = request.POST.get('product_id')
            comment = request.POST.get('comment')

            print("the ratings are " , ratings)

            try :
                data = Product.objects.filter(pid = p_id)
            except Exception as e :
                return render(request , '404.html')

            if len(data) == 0:
                return render(request , '404.html')
            else:
                today = date.today()
                d2 = today.strftime("%B %d, %Y")

                p_data = Product.objects.filter(pid = p_id)

                if len(Comment.objects.filter(userid = request.user , pid = p_data[0])) > 0 :

                    Comment.objects.create(pid = p_data[0] , userid = request.user , comment = comment , ratings = 0 , added_date = d2)
                    return redirect('/')
                else:

                    if ratings == None:
                        Comment.objects.create(pid = p_data[0] , userid = request.user , comment = comment , ratings = 0 , added_date = d2)
                        return redirect('/')
                    else:
                        Comment.objects.create(pid = p_data[0] , userid = request.user , comment = comment , ratings = ratings , added_date = d2)
                        return redirect('/')

        else:
            return redirect('/login')

    else:

        return redirect('/login')



        



