from django.shortcuts import render
from .models import Product, Category

def catalog_view(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.all()
    
    if category_slug:
        products = products.filter(category__slug=category_slug)
    
    return render(request, 'goods/catalog.html', {
        'products': products,
        'categories': categories,
        'current_category': category_slug
    })