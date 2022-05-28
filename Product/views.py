from django.shortcuts import render
from Product.models import *
import random


def Index(request):
    New_product = Product.objects.all().reverse()
    Women_product = Product.objects.filter(category__name='nu')
    Men_product = Product.objects.filter(category__name='nam')
    Fashion_product = Product.objects.filter(tags__name='fashion')

    return render(request, 'queenok/index.html',
                  {'New_product': New_product,
                   'wm_product': Women_product,
                   'm_product': Men_product,
                   'fs_product': Fashion_product

                   }
                  )


def CategoryView(request, id):
    categories = Category.objects.all().order_by('name')
    product = Product.objects.filter(category__id=id) or Product.objects.filter(category__name=id)
    New_product = Product.objects.all().reverse()
    New_product1 = New_product[0:3]
    New_product2 = New_product[3:6]
    New_product3 = New_product[6:9]
    New_product4 = New_product[9:12]

    return render(request, 'queenok/category_page.html',
                  {
                      'categories': categories,
                      'Product': product,
                      'New_product1': New_product1,
                      'New_product2': New_product2,
                      'New_product3': New_product3,
                      'New_product4': New_product4,

                  })


def CategoryBase(request):
    categories = Category.objects.all().order_by('name')
    product = Product.objects.all().order_by('?')
    product = product[0:8]
    New_product = Product.objects.all().order_by('?')
    New_product1 = New_product[0:3]
    New_product2 = New_product[3:6]
    New_product3 = New_product[6:9]
    New_product4 = New_product[9:12]

    return render(request, 'queenok/category_page.html',
                  {
                      'categories': categories,
                      'Product': product,
                      'New_product1': New_product1,
                      'New_product2': New_product2,
                      'New_product3': New_product3,
                      'New_product4': New_product4,

                  })


def ContactUs(request):
    return render(request, 'queenok/contact_us.html')


def Detail(request, id):
    product_detail = Product.objects.filter(id=id)
    for i in product_detail:
        print(i.image_link)
        cate = i.category
    product_related = Product.objects.filter(category__name=cate)
    New_product = Product.objects.all().reverse()
    New_product1 = New_product[0:3]
    New_product2 = New_product[3:6]
    categories = Category.objects.all().order_by('name')
    return render(request, 'queenok/product_detail_page.html',
                  {'product_detail': product_detail,
                   'product_related': product_related,
                   'New_product1': New_product1,
                   'New_product2': New_product2,
                   'categories': categories,
                   }
                  )


def SingleBlog(request):
    return render(request, 'queenok/single_blog.html')


def BlogPage(request):
    return render(request, 'queenok/blog_page.html')


def About(request):
    return render(request, 'queenok/about.html')
