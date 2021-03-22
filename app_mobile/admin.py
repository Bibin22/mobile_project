from django.contrib import admin

# Register your models here.
from .models import Mobile,Order
admin.site.register(Mobile)
admin.site.register(Order)