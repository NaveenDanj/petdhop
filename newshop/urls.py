"""newshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static


from auth import views
from product import views as p
from cart import views as c
from wishlist import views as w
from search import views as s
from compare import views as cp
from account import views as acc
from checkout import views as check
from dashboard import views as dashboard

urlpatterns = [

    path('' , views.homepage),
    path('admin/', admin.site.urls),
    path('login-register/' , views.login_register),
    path('login_handle/' , views.login_handle ),
    path('register_handle/' , views.reg_handle),
    path('login/' , views.login_page),
    path('logout/' , views.logout_user),
    path('register/' , views.register_page),
    path('product_details/' , p.product_details),
    path('handle_comment/' , p.add_comment),
    path('add_to_cart/' , c.add_to_cart),
    path('del_item_cart/' , c.del_cart_item),
    path('wishlist/' , w.wishlist_page),
    path('add_wish/' , w.add_wish),
    path('del_wish/' , w.del_wish),
    path('cart/' , c.cart_page),
    path('update_cart/' , c.update_cart),
    path('reset_cart/' , c.reset_cart),
    path('search/' , s.search_page),
    path('compare/' , cp.compare_page),
    path('add_compare/' , cp.add_compare),
    path('delete_compare/' , cp.delete_compare),
    path('account/' , acc.acoount_page),
    path('update_account/' , acc.update_account),
    path('checkout/' , check.checkout_page),
    path('place_order/' , check.place_order),
    path('dashboard/' , dashboard.dashboard_page),
    path('dashboard-login/' , dashboard.dashboard_login_page),
    path('dash_login/' , dashboard.dashboard_login),
    path('return/' , check.success_payment),
    path('dash-back/' , dashboard.dash_back_page),
    path('add_product/' , dashboard.add_product),
    path('add_cat/' , dashboard.add_cat),
    path('search_product/' , dashboard.search_product),
    path('delete_product/' , dashboard.delete_product),
    path('edit_product/' , dashboard.edit_product_page),
    path('ed_p/' , dashboard.edit_product),
    path('view_order/' , dashboard.view_order),
    path('mark_as_completed/' , dashboard.mark_complete),
    path('cancel_order/' , dashboard.cancel_order),
    path('product_report/' , dashboard.product_report_page)



]


urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)