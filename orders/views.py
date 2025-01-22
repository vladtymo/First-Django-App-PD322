import datetime
from django.shortcuts import redirect, render

from cart.cart import get_cart
from orders.models import Order
from users.models import User

def index(request):
    orders = Order.objects.all()

    # filter: model__field
    # orders = Order.objects.filter(client__name="Vlad")

    return render(request, "orders/index.html", {"orders": orders})

def confirm(request):
    
    items = get_cart(request.session)
    users = User.objects.filter(id__in=items.keys())

    Order.objects.create(
        # TODO: use product price
        total_price = users.count() * 100,
        client = User.objects.last()
    )

    return redirect("/orders")