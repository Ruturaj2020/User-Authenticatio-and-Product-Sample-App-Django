from django.contrib import admin
from .models import postview
from products.models import productview
# Register your models here.

admin.site.register(postview)
admin.site.register(productview)