from django.shortcuts import get_object_or_404, redirect, render

from .forms import BrandForm
from .models import Product, Review
from django.utils.text import slugify

# Create your views here.
def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    r = Review.objects.get(fk_product = product.product_id)
    return render(request, 'product/product.html', {'product':product, 'n': range(r.stars)})

def review_text(request):
    # request.product_id
    # prodID = Product.objects.get(product_id = request.product.product_id)
    if request.method == 'POST':
        reviewText = request.POST.get('reviewText')
        stars = request.POST.get('stars')        
        prodID = request.POST.get('product')
        r = Review.objects.create(review = reviewText, stars = stars, fk_product = prodID.product_id)
        r.save() 

    return render(request, 'core/myaccount.html')

def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        # form2 = ProductForm(request.POST)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.fk_user = request.user
            brand.slug = slugify(brand.brand_name)
            brand.save()
            # product = form2.save(commit=False)
            # product.fk_user = request.user
            # product.slug = slugify(product.product_name)
            # product.fk_brand = brand
            # product.save()


    return render(request, 'product/add_product.html')