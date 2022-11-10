from django.contrib import admin
from .models import Order, OrderDetail, Return

admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Return)