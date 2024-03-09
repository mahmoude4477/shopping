"""
URL configuration for shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from phone import views
from books import views as books

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('showphone/',views.showphone,name='showphone'),
    path('detals/<int:id>/',views.detals,name='detals')
    ,path('auth-login/',views.auth_login,name='auth-login')
    ,path('auth-register/',views.auth_register,name='auth-register'),
    path('logout/',views.logout_view,name='logout'),
    path('checkout/',views.checkout,name='checkout'),
    path('add_to_cart/<int:id>',views.add_to_cart,name='add_to_cart'),
    path('remove_from_cart/<int:id>',views.remove_from_cart,name='remove_from_cart'),
    # books
    path('add_to_cart_b/<int:id>',books.add_to_cart,name='add_to_cart_b'),
    path('remove_from_cart_b/<int:id>',books.remove_from_cart,name='remove_from_cart_b'),
    path('showBooks/',books.showBooks,name='showBooks'),
    path('detals_b/<int:id>/',books.detals,name='detals_b'),
     path('checkout_b/',books.checkout,name='checkout_b'),
     path('inv/',books.inv,name='inv'),
     path('done/',books.done,name='done'),
     
]
