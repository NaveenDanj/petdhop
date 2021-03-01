from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate , login , logout
from account.models import Account
from dashboard.models import Notification
from product.models import *
from API.getter import *

# Create your views here.


def login_register(request):

    form = CreateUserForm()

    context = {"reg_form" : form}

    return render(request , 'login_register.html' , context)



def login_page(request):

    if request.method == 'POST':

        login_username = request.POST.get('username')
        login_password = request.POST.get('password')

        user = authenticate(request , username = login_username , password = login_password)

        if user is not None :
            login(request , user)
            return redirect('/')
        else:
            messages.info(request , "Username or password is incorrect")
            return render(request , 'login.html')

    return render(request , 'login.html')



def register_page(request):
    form = CreateUserForm()

    context = {"reg_form" : form}

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if password1 == password2 : 
            
            if User.objects.filter(username = username).exists():
                messages.info(request , "Username already taken")
            elif User.objects.filter(email = email).exists():
                messages.info(request , "Email already taken")

        else:
            messages.info(request , "Passwords doesn't match")



        if form.is_valid():
            form.save()
            user = User.objects.filter(username = username , email = email)[0]
            Account.objects.create(user_id = user)
            Notification.objects.create(notify_type = 'User Signup' , notify_text = username + " has created an account")
            return redirect('/')
        else:
            messages.info(request , "Error Creating User...Check your inputs!")

           

    return render(request , 'register.html' , context)


def logout_user(request):
    logout(request)
    return redirect('/login')



def login_handle(request):

    if request.method == 'POST':
        
        login_username = request.POST.get('username')
        login_password = request.POST.get('password')

        user = authenticate(request , username = login_username , password = login_password)

        if user is not None :
            login(request , user)
            return redirect('/')
        else:
            messages.info(request , "Username or password is incorrect")

        return redirect('/login-register')


    return redirect('/login-register')



def reg_handle(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        else:

            return render(request , 'login_register.html' , )


        return redirect('/')

    return redirect('/login-register')


def homepage(request):

    if  request.user.is_authenticated :

        print("the famous cats are" , get_top_categories())

        data = {'top_cats' : get_top_categories() ,  "all_cats" : get_all_categories() , 'new_products' : get_new_products() , 'cart_data' : get_cart_data(request.user)[0] , 'all_items' : len(get_cart_data(request.user)[0]) , 'total_price' : get_cart_data(request.user)[1] }

        return render(request , 'home.html' , data)

    return redirect('/login')
