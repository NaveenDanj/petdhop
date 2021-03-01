from product.models import *
from account.models import *
from checkout.models import *
from cart.models import *


def get_all_categories():

    return Category.objects.all()


def get_new_products():
    data = []
    products = Product.objects.all()[:5]

    for i in range(len(products)-1 , -1 , -1):
    
        data.append(get_single_product(products[i].pid))

    return data



def get_single_product(pidd):
    
    p = Product.objects.get(pid = pidd)
    thmb = Product_Image.objects.filter(product_id = p)[0]
    cat = []
    cat = Product_Category.objects.filter(product_id = p)

    return {'data' : p , 'thumb' : thmb , 'cats' : cat }



def get_cart_data(user):
    cart_data = Cart.objects.filter(user_id = user )

    total = 0
    c_data = []

    for item in cart_data:

        p = item.product_id
        thmb = Product_Image.objects.filter(product_id = p)[0]
        c_data.append({'data' : item , 'image' : thmb})

        total = total + item.product_id.new_price * item.amount

    return [c_data , total]


def get_customer_full_review(product):

    alls = Comment.objects.filter(pid = product)

    full_ratings = 0

    for item in alls:

        full_ratings = full_ratings + item.ratings


    if len(alls) > 0 :
        return round(full_ratings / len(alls))
    else:
        return 0


def get_all_products():

    ret = []

    alls = Product.objects.all()

    for item in alls:

        ret.append(get_single_product(item.pid))

    return  sorted(ret, key=lambda k: k['data'].stocks , reverse=True)



def get_top_categories():

    products = Product.objects.all()

    cats = Category.objects.all()

    cats_with_marks =[]

    for cat in cats:

        total = 0

        total_products = Product_Category.objects.filter(cat_id = cat)

        for product in total_products:

            total += product.total_sales

        cats_with_marks.append({'cat' : cat , "mark" : total})

    return sorted(cats_with_marks, key=lambda k: k['mark'] , reverse=True)[:6]






