from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from .models import Category, Product, Promotion
from django.urls import reverse
from django.shortcuts import render
from .forms import ProductSearchForm


# Create your views here.


menu =[{'title': "Каталог", 'url_name': 'catalog_url'},
       {'title': "О компании", 'url_name': 'about_main'},
       {'title': "Оптовикам", 'url_name': 'wholesaler'},
       {'title': "Розница", 'url_name': 'retail'},
       {'title': "Качество", 'url_name': 'quality'},
       {'title': "Контакты", 'url_name': 'contacts'},
       {'title': "ВкусВилл", 'url_name': 'vkusvil'}
]
products = Product.objects.all()
dictionary = {
    "menu": menu,
    "products": products,
    "title": 'Главная страница'
    }

def index(request):
 
    return render(request, 'index.html', context = dictionary)


def catalog(request):
    # products = Product.objects.all() 
    return render(request, 'catalog.html', context = dictionary)




def catalog(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    promotions = Promotion.objects.filter(product__in=products)

    if 'query' in request.GET:
        form = ProductSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            products = products.filter(title__icontains=query)
    else:
        form = ProductSearchForm()

    context = {
        'categories': categories,
        'products': products,
        'promotions': promotions,
        'form': form,
    }
    return render(request, 'catalog.html', context)
















def wholesaler(request):
    return render(request, 'wholesaler.html')

def about_main(request):
    return render(request, 'about_main.html', {"menu": menu, "title": 'О компании'})



def retail(request):
    return render(request, 'retail.html')

def quality(request):
    return render(request, 'quality.html')

def contacts(request):
    return render(request, 'contacts.html')

def show_products(request, product_id):
    products = get_object_or_404(Product, pk=product_id)

    dictionary = {
    "products": products,
    "title": products.title, 
    "category_selected": products.categorys_id,
    }

    return render(request, 'products.html', context=dictionary)


def vkusvil(request):
    return render(request, 'vkusvil.html')