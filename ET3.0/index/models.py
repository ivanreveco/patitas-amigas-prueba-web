from django.db import models

# Create your models here.
class cliente(models.Model):# TABLA CLIENTE (PARA REGISTRO Y INICIAR SESSION)
    Id_cliente = models.AutoField(primary_key=True)#Llave primaria
    Nombre = models.CharField(max_length= 200)
    Apellido = models.CharField(max_length= 200)
    Correo = models.CharField(max_length= 200)
    Contraseña = models.CharField(max_length= 200)
    Edad = models.IntegerField()
    
    def __str__(self) :
        return self.Nombre
    class meta:# PARA GUARDAR UN NOMBRE EN LA TABLA Y QUE NO SE GUARDE CON EL PREFIJO CREADO POR DJANGO
        db_table = 'cliente'
        
class articulos(models.Model):#TABLA PARA LOS PRODUCTOS DE LA PAGINA
    Id_producto =models.AutoField(primary_key=True)#Llave primaria
    Nombre_P=models.CharField(max_length=200)
    Presio_P=models.IntegerField()
    Descripcion=models.CharField(max_length=200)
    Cantidad=models.IntegerField()
    img=models.CharField(max_length=2000,null=True,default='-')
    
    def __str__(self):
        return self.Nombre_P
    class meta:
        db_table='articulo'

class carrito(models.Model):#TABLA PARA EL CARRITO DONDE SE GUARDAN LOS PRODUCTOS QUE EL CLIENTE SELECCIONA
    Id_carrito=models.AutoField(primary_key=True)#Llave primaria
    Precio_carrito=models.IntegerField()
    Id_cliente=models.ForeignKey(cliente, on_delete=models.CASCADE, db_column='cliente_id_cliente', default=1000)
    Id_producto=models.ForeignKey(articulos, on_delete=models.CASCADE, db_column='Producto_id_Producto', default= 1000)
    def __str__(self):
         return self.Precio_carrito
    class meta:
        db_table='Carrito'
     
