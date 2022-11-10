from django.shortcuts import redirect, render
from .models import Order, OrderDetail
from cart.cart import Cart
from core.models import Address

def start_order(request):
    cart = Cart(request)
    if request.method == 'POST':

        addressLine1 = request.POST.get('addressLine1')
        addressLine2 = request.POST.get('addressLine2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        total = request.POST.get('total')


        address = Address.objects.create(fk_user = request.user, addressLine1 = addressLine1, addressLine2 = addressLine2, city = city, state = state, zipcode = zip)
        address.save()
        order = Order.objects.create(fk_user=request.user, total = total)

        for item in cart:
            fk_product = item['product']
            quantity = int(item['quantity'])
            price = fk_product.price * quantity
            # fk_status_id = StatusTypes.objects.filter(status_name = 'Ordered').values_list('pk', flat=True)

            item = OrderDetail.objects.create(fk_order=order, status = "Ordered", fk_brand = fk_product.fk_brand, fk_user = fk_product.fk_user, fk_product = fk_product, price = price, quantity = quantity)

        cart.clear()

        return redirect('myaccount')
    return redirect('cart')