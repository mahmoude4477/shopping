from django.contrib import admin
from .models import Cart, books
# Register your models here.

admin.site.register(books)
admin.site.register(Cart)