from django.shortcuts import render, redirect
from .forms import *
from django.contrib import auth
import logging
from datetime import datetime

logging.basicConfig(filename="sample.log", level=logging.INFO)


# Create your views here.
def product(request, product_id):
    product = Product.objects.get(id=product_id)
    username = auth.get_user(request).username
    print(request.path)
    return render(request, 'products/product.html', locals())


def change_product(request, product_id):
    print(request.path)

    form = Change(request.POST or None)
    username = auth.get_user(request).username
    if request.POST and form.is_valid():
            Change_product = Product.objects.filter(id=product_id).update(price=request.POST.get('price'),
                                                                        discount=request.POST.get('discount'),
                                                                        description=request.POST.get('description'),
                                                                          short_description=request.POST.get('short_description'),
                                                                          )
            logging.info("the book was changed \n date - %s %s %s" % (request.POST.get('update_month'),request.POST.get('update_day'),request.POST.get('update_year')))
            return redirect('/')
    return render(request, 'products/change_book.html', locals())


def home(request):
    username = auth.get_user(request).username
    products_images_new = Product.objects.all()[0:4]
    products_images = Product.objects.filter(is_active=True)
    products_images_romans = products_images.filter(category__id=1)
    products_images_povest = products_images.filter(category__id=2)
    print(request.path)
    return render(request, 'products/home_page.html', locals())


def add_new(request):
    print(request.path)

    username = auth.get_user(request).username
    form = AddNewBook(request.POST, request.FILES)
    if request.method == 'POST':
        form = AddNewBook(request.POST, request.FILES)
        if form.is_valid():
            if 'photo' in request.FILES:
                form.photo = request.FILES['photo']
                logging.info(("the book was added date - %s \n" % (datetime.now())))
            form.save(commit=True)
            return redirect('/')
        else:
            print(form.errors)

    return render(request, 'products/add_new_book.html', locals())

def sorted_by_data(request):
    username = auth.get_user(request).username
    products_images = Product.objects.all()
    if request.POST:
        value = request.POST['engine']
        products_images = Product.objects.order_by(value)
        print(request.path)
        print(value)
        return render(request, 'products/all_books.html', locals())

    return render(request, 'products/all_books.html', locals())


