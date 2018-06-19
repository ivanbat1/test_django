from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def product(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, 'product.html', locals())


def change_product(request, product_id):
    form = Change(request.POST or None)
    if request.POST and form.is_valid():

            Change_product = Product.objects.filter(id=product_id).update(price=request.POST.get('price'),
                                                                        discount=request.POST.get('discount'),
                                                                        description=request.POST.get('description'),
                                                                          short_description=request.POST.get('short-description')
                                                                          )
            return redirect('/')
    return render(request, 'change_book.html', locals())


def home(request):
    products_images_new = Product.objects.all()[0:4]
    products_images = Product.objects.filter(is_active=True)
    products_images_romans = products_images.filter(category__id=1)
    products_images_povest = products_images.filter(category__id=2)
    import sqlite3 as lite

    con = lite.connect('db.sqlite3')

    with open('adding.txt', 'w+') as f:
        cur = con.cursor()
        cur.execute("SELECT * FROM books_product")
        rows = cur.fetchall()

        for row in rows:
            print(row)


    return render(request, 'home_page.html', locals())


def add_new(request):
    form = AddNewBook(request.POST, request.FILES)
    if request.method == 'POST':
        form = AddNewBook(request.POST, request.FILES)
        if form.is_valid():
            if 'photo' in request.FILES:
                form.photo = request.FILES['photo']
            form.save(commit=True)
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'add_new_book.html', {'form': form})

def sorted(request):
    products_images = Product.objects.all()
    if request.POST:
        value = request.POST['engine']
        products_images = Product.objects.order_by(value)
        print(value)
        return render(request, 'all_books.html', locals())

    return render(request, 'all_books.html', locals())


