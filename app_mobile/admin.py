from django.contrib import admin

# Register your models here.
from .models import Mobile,Order,Cart
admin.site.register(Mobile)
admin.site.register(Order)
admin.site.register(Cart)