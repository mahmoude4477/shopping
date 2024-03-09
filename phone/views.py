import datetime
from django.shortcuts import render,redirect

from phone.form import UserCreateForm,UserLoginForm
from .models import items, itemsDetails,Cart
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@csrf_exempt 
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('auth-login')
@csrf_exempt
def auth_login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                if user.is_active:
                    user.last_login = datetime.datetime.now()
                    user.save()
                    
                    login(request, user)
                    return redirect('index')
        else:
            print(form.errors)
    elif request.user.is_authenticated:
            return redirect('index')

            
    value = {'form': form}
    return render(request, 'auth_login.html', value)



@csrf_exempt
def auth_register(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth-login')
        else:
            print(form.errors)

    value = {'form': form}
    return render(request, 'auth-register.html', value)

def index(request):
    return render(request, 'index.html')

def showphone(request):
    itemsList = items.objects.all()
    all_items_details = itemsDetails.objects.prefetch_related('itemsId')
    
    value = {'itemsList': itemsList, 'itemsDetailsList': all_items_details}
    return render(request, 'showphone.html', value)

def detals(request,id):
    itemsList = items.objects.all()
    print(id)
    all_items_details = itemsDetails.objects.prefetch_related('itemsId').filter(id=id)
    value = {'itemsDetailsList': all_items_details}
    return render(request, 'detals.html',value)

@login_required(login_url='auth-login',redirect_field_name='next')
def checkout(request):
    current_user = request.user.id
    cartD = Cart.objects.all().filter(userId=current_user)
    total = 0
    for i in cartD:
        total += i.net
    value = {'cartD': cartD, 'total': total}
    return render(request, 'checkout.html', value)

def add_to_cart(request, id):
    discount = 0
    qty = 1
    current_user = request.user.id
    items_details = itemsDetails.objects.select_related('itemsId').get(id=id)
    cartD = Cart.objects.all().filter(userId=current_user)
    if cartD.filter(itemsDetailsId=id).exists():
        cart = cartD.get(itemsDetailsId=id)
        cart.qty += 1
        cart.total += items_details.total
        cart.price += items_details.price
        cart.discount = discount
        cart.net = cart.price - discount
        cart.save()
        return redirect('showphone')
    cart = Cart.objects.create(
        itemsDetailsId=items_details,
        qty=qty,
        total=items_details.total,
        price=items_details.price,
        discount=discount,
        net=items_details.price - discount,
        status=False,
        userId=current_user,
    )
    cart.save()
    return redirect('showphone')
def remove_from_cart(request, id):
    request.session["cart_count"] = Cart.objects.filter(userId=request.user.id).count()
    current_user = request.user.id
    cartD = Cart.objects.all().filter(userId=current_user)
    cartD.filter(id=id).delete()
    return redirect('checkout')
