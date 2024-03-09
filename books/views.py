from django.shortcuts import render,redirect

from books.models import Cart, books, doneBuy
from django.contrib.auth.decorators import login_required

# Create your views here.
def showBooks(request):
    itemsList = books.objects.all()

    value = {'itemsList': itemsList,}
    return render(request,'showbooks.html',value)

def detals(request,id):
    itemsList = books.objects.all().filter(id=id)
    value = {'itemsList': itemsList}
    return render(request, 'detals_b.html',value)


def add_to_cart(request, id):
    current_user = request.user.id
    items_details = books.objects.get(id=id)
    cart = Cart.objects.create(
        bookId=items_details,
        userId=current_user
    )
    cart.save()
    return redirect('showBooks')
def remove_from_cart(request, id):
    current_user = request.user.id
    cartD = Cart.objects.all().filter(userId=current_user)
    cartD.filter(id=id).delete()
    return redirect('checkout_b')

@login_required(login_url='auth-login',redirect_field_name='next')
def checkout(request):
    current_user = request.user.id
    cartD = Cart.objects.all().filter(userId=current_user)
    total = 0
    for i in cartD:
        total += i.bookId.price
    value = {'cartD': cartD, 'total': total}
    return render(request, 'checkout_b.html', value)
def done(request):
    current_user = request.user.id
    cartD = Cart.objects.all().filter(userId=current_user)
    for i in cartD:
        done = doneBuy.objects.create(
            bookId=i.bookId,
            userId=current_user
        )
        done.save()
    cartD.delete()
    return redirect('inv')
def inv(request):
    current_user = request.user.id
    done = doneBuy.objects.all().filter(userId=current_user)
    if len(done) == 0:
        value = {'done': 'No items'}
    else:
        value = {'done': done.last()}
    return render(request, 'inv.html', value)