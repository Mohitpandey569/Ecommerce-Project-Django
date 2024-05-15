from django.contrib import admin
from . models import Products ,CartItem ,Order ,Address
# Register your models here.
admin.site.register(Products)
admin.site.register(CartItem)
admin.site.register(Address)


class OrderAdmin(admin.ModelAdmin):
    list_display =["product_id","quantity","user","is_completed"]
admin.site.register(Order,OrderAdmin)