from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from product.models import *
from account.models import *
from checkout.models import *
from django.http import HttpResponseRedirect
from dashboard.models import *

from API.getter import *

# Create your views here.
def dashboard_page(request):

    if request.user.is_superuser:

        all_accounts = Account.objects.all()
        all_orders = Order.objects.filter(status = 'Completed')
        orders_pending = Order.objects.filter(status = 'Pending')
    
        recent_orders = Order.objects.all()

        ro = []

        for i in range(len(recent_orders)-1 , -1, -1):
            ro.append(recent_orders[i])

        total_rev = 0

        for item in all_orders:

            total_rev = total_rev + item.total

        sold_by_units = Product.objects.all().order_by('total_sales')[:7]
        top_products = Product.objects.all().order_by('total_sales')[:4]

        tp = []

        for item in top_products :

            image = Product_Image.objects.filter(product_id = item)[0]

            tp.append({"item" : item , "image" : image})


        new_customer_orders = Order.objects.all()[:5]

        new_customer = []

        unique_user = []

        for customer in new_customer_orders:

            if customer.user_id.username not in unique_user:

                unique_user.append(customer.user_id.username)

                user = customer.user_id

                total_orders = len(Order.objects.filter(user_id = user))

                user_order = Order.objects.filter(user_id = user , status = 'Completed')

                total_gain = 0

                for o in user_order :
                    total_gain = total_gain + o.total

                new_customer.append({"user" : user , "total_orders" : total_orders , "total_gain" : total_gain })

        notifies = []

        recent_not = Notification.objects.all()[:7]

        for i in range(len(recent_not)-1 , -1, -1):
            notifies.append(recent_not[i])




        obj = {"total_users" : len(all_accounts) , "total_orders" : len(all_orders) ,  "total_revenue" : total_rev , "orders_pending" : len(orders_pending) , "ro" : ro , "so" : sold_by_units , "tp" : tp , "new_customer" : new_customer , "notifies" : notifies , 'notify_len' : len(notifies) }


        return render(request , 'admin/home.html' , obj)

    else:
        return redirect('/')



def dashboard_login_page(request):

    return render(request , 'admin/dash_login.html')



def product_report_page(request):
    
    data = {'products' : get_all_products()}

    return render(request , 'admin/product_sales.html' , data)




def dashboard_login(request):

    if request.method == 'POST':

        login_username = request.POST.get('username')
        login_password = request.POST.get('password')

        user = authenticate(request , username = login_username , password = login_password)

        if user is not None :
            if user.is_superuser:
                login(request , user)
                return redirect('/dashboard')
            else:
                messages.info(request , "You are not allowed to Login to Dashboard")
                logout(request)

        else:
            messages.info(request , "Username or password is incorrect")
            return redirect('/dashboard-login')

    return redirect('/dashboard-login')



def add_product(request):
    
    if request.user.is_superuser :
        if request.method == 'POST':

            name = request.POST.get('name')
            short = request.POST.get('short')
            long_ = request.POST.get('long')
            old = request.POST.get('old_price')
            new = request.POST.get('new_price')
            stocks = request.POST.get('stocks')
            tags = request.POST.get('tags')
            categories = request.POST.getlist('categories')

            uploaded_files = request.FILES.getlist('images')

            p = Product.objects.create(name = name , short_desc = short , long_desc = long_ , old_price = old , new_price = new  , tags = tags , stocks = stocks)

            for cat in categories:
                
                cat_obj = Category.objects.get(category_id = cat)

                Product_Category.objects.create(product_id = p , cat_id = cat_obj)



            for image in uploaded_files:
                
                img = Image.objects.create(image_file = image)

                Product_Image.objects.create(product_id = p , image_id = img)


            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_cat(request):

    if request.user.is_superuser:
        if request.method == 'POST':

            cat_name = request.POST.get('name')
            cat_img = None 

            try:
                cat_img = request.FILES.get('img')
                Category.objects.create(cat_name = cat_name , cat_img = cat_img)
            except :
                return render(request , '404.html')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            
def dash_back_page(request):

    if request.user.is_superuser:

        cat = Category.objects.all()

        obj = {"cat" : cat}

        return render(request , 'admin/add_back.html' , obj)


def search_product(request):

    if request.user.is_superuser:

        if request.method == 'POST':

            q = request.POST.get('q')

            if q == None or q == '' :
                return redirect('/dash-back')


            alls =[ Product.objects.filter(name__icontains = q )]

            cat = Category.objects.all()

            obj = {"cat" : cat , 'search' : alls , 'len': len(alls) }

            return render(request , 'admin/add_back.html' , obj)
        else:
            return redirect('/dash-back')


def edit_product_page(request):

    if request.user.is_superuser:

        if request.GET.get('pid') != None or request.GET.get('pid') != '':

            pid = request.GET.get('pid')

            try:
                
                p = Product.objects.get(pid = pid)

                obj = {"p" : p}

                return render(request , 'admin/edit_product.html' , obj)

            except Exception as e:

                print("the error is " , e )

                return render(request , '404.html')
        else:
            return render(request , '404.html')


def edit_product(request):

    if request.method == 'POST':

        if request.user.is_superuser:

            name = request.POST.get('name')
            old_price = request.POST.get('old_price')
            new_price = request.POST.get('new_price')
            tags = request.POST.get('tags')
            short = request.POST.get('short')
            longg = request.POST.get('long')
            stocks = request.POST.get('stocks')
            pid = request.POST.get('pid')


            if len(name) > 0 and len(old_price) > 0 and len(new_price) > 0 and len(tags) > 0 and len(short) > 0 and len(longg) > 0 and len(stocks) > 0:

                try:

                    p = Product.objects.get(pid = pid)
                    p.name = name
                    p.old_price = int(old_price)
                    p.new_price = int(new_price)
                    p.tags = tags
                    p.short_desc = short
                    p.long_desc = longg
                    p.stocks = stocks

                    p.save()

                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                except Exception as e:

                    print("the error is " , e )

                    return render(request , '404.html')

            else:

                return render(request , '404.html')

        

def delete_product(request):

    if request.method == 'POST':

        if request.user.is_superuser:

            pid = request.POST.get('pid')

            if pid == '' or pid == None:
                return render(request , '404.html')
            else:
                
                p = Product.objects.filter(pid = pid)[0]

                Product_Image.objects.filter(product_id = p).delete()
                Product_Category.objects.filter(product_id = p).delete()
                Comment.objects.filter(pid = p).delete()

                p.delete()

                return redirect('/dash-back')


def mark_complete(request):

    if request.user.is_superuser:
        if request.method == 'POST':
            try:
                o = Order.objects.get(order_id = request.POST.get('order_id'))
                o.status = 'Completed'
                o.save()

                order_pr = Order_Product.objects.filter(order_id = o)

                for item in order_pr:

                    p = item.product_id
                    p.total_sales = p.total_sales +  item.amount
                    p.stocks = p.stocks - item.amount
                    p.save()

                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except Exception as e:
                print("the error is " , e)
                return render(request , '404.html')


def cancel_order(request):

    if request.user.is_superuser:
        if request.method == 'POST':
            try:
                o = Order.objects.get(order_id = request.POST.get('order_id'))
                o.status = 'Canceled'
                o.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except Exception as e:
                print("the error is " , e)
                return render(request , '404.html')



def view_order(request):

    if request.user.is_superuser:
        
        if request.GET.get('order_id') != None and request.GET.get('order_id') != '':

            try :

                order_id = request.GET.get('order_id')
                o = Order.objects.get(order_id = order_id)

                all_products = Order_Product.objects.filter(order_id = o)
                user = o.user_id

                user_account = Account.objects.get(user_id = user )

                obj = {"order" : o , "order_products" : all_products , 'account' : user_account }

                return render(request , 'admin/order_view.html' , obj)
                
            except Exception as e:
                print("the error is" , e)
                return render(request , '404.html')