from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.db.models import Q
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from products.models import Product, Category
from django.contrib.auth.models import Group

def frontpage(request):
    products = Product.objects.all()
    return render(request, 'core/frontpage.html', {'products': products})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        group_name = request.POST['group_name']
        if form.is_valid():
            user = form.save()
            user.save()
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

@login_required
def myaccount(request):
    return render(request, 'core/myaccount.html')
    
def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    active_category = request.GET.get('category', '')
    if active_category:
        products = products.filter(fk_category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        products = products.filter(Q(product_name__icontains=query) | Q(descrpt__icontains = query))
    context = {'categories': categories, 'products': products, 'active_category': active_category}
    return render(request, 'core/shop.html', context)

def seller(request):
    products = Product.objects.all()
    # od = OrderDetail.objects.all()

    # get_price = od.filter(fk_product = products.)

    # totalSale = sum(get_price)

    return render(request, 'core/seller.html', {'products': products})