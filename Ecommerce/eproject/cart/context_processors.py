from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    item_count = 0
    try:
        cart = Cart.objects.filter(cart_id=_cart_id(request))
        car_items = CartItem.objects.all().filter(cart=cart[:1])
        for item in car_items:
            item_count += item.quantity
    except Cart.DoesNotExist:
        item_count = 0
    return dict(item_count=item_count)
