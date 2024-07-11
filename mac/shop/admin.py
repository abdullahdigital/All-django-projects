# admin.py

from django.contrib import admin
from .models import Product, Contact, Orders, OrderUpdate
from .forms import ProductAdminForm

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

admin.site.register(Product, ProductAdmin)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
