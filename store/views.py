from django.shortcuts import render, get_object_or_404
from .models import Category, Product
# Create your views here.

# For return all products information
def all_products(request):
    products = Product.objects.all()
    
    return render(request, 'store/home.html', {'products':products})



# For product details
def product_detail(request, slug):
    product =  get_object_or_404(Product, slug= slug, in_stock = True)
    return render(request, 'store/product/detail.html', {'product':product})

# For Category List

def category_list(request,category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    products = Product.objects.filter( category= category ) 
    return render(request, 'store/product/category.html', {'category': category, 'products':products})