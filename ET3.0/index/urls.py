from django.urls import path
from . import views

app_name= 'index'

urlpatterns =[
     path('',views.home, name="home"),
     path('inicio/',views.inicio, name="inico"),
     path('registro/',views.registro, name="registro"),
     path('tienda/',views.tienda, name="tienda"),
     path('carrito/',views.Carrito, name="carrito"),
     
     
     
]