from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Category, Product, Promotion
from .forms import ProductSearchForm


menu = [
    {'title': "Каталог", 'url_name': 'catalog_url', 'active': True},
    {'title': "О компании", 'url_name': 'about_main'},
    {'title': "Оптовикам", 'url_name': 'wholesaler'},
    {'title': "Розница", 'url_name': 'retail'},
    {'title': "Качество", 'url_name': 'quality'},
    {'title': "Контакты", 'url_name': 'contacts'},
    {'title': "ВкусВилл", 'url_name': 'vkusvil'},
]

dictionary = {
    "menu": menu,
    "products": Product.objects.all(), # это необходимо перенести в функцию
    "title": 'Главная страница',
}


class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = kwargs
        context.update(dictionary)
        return super().get_context_data(**context)


class LoginRequiredView(LoginRequiredMixin, BaseView):
    # login_url = reverse('login_options')
    login_url = '/accounts/login_options/'


class IndexView(BaseView):
    template_name = 'index.html'


class LoginOptionsView(BaseView):
    template_name = 'login_options.html'


class EmailConflictView(BaseView):
    template_name = 'account_email_conflict.html'


class AccountView(LoginRequiredView):
    template_name = 'account.html'


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
