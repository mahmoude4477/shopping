

from phone.models import Cart


def cart_count(request):
    cart_count = Cart.objects.filter(userId=request.user.id).count()  # Assuming you have a 'user' field in your CartItem model
    return {'cart_count': cart_count}