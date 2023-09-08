from django.contrib import admin
from .models import cliente,articulos,carrito
# Register your models here.

admin.site.register(cliente)
admin.site.register(articulos)
admin.site.register(carrito)

