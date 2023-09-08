from django.contrib.auth import authenticate, login
from django import forms
from django.shortcuts import redirect, render
from .models import articulos,cliente,carrito
from .forms import LoginForm, RegistroForm
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


def home(request):
    return render(request, "INDEX.HTML")



def Carrito(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        
        if producto_id:
            try:
                producto = articulos.objects.get(Id_producto=producto_id)
                
                cliente_actual = cliente.objects.get(Id_cliente=2)  # Obtener el cliente actual (puedes cambiar el ID según tus necesidades)
                
                carrito_obj = carrito.objects.create(Precio_carrito=producto.Presio_P, Id_cliente=cliente_actual, Id_producto=producto)
                carrito_obj.save()
                
                return redirect('index:carrito')
            except articulos.DoesNotExist:
                pass
        
        return redirect('index:tienda')
    
    if request.method == 'GET' and 'borrar_carrito' in request.GET:
        cliente_actual = cliente.objects.get(Id_cliente=2)  # Obtener el cliente actual (puedes cambiar el ID según tus necesidades)
        carrito.objects.filter(Id_cliente=cliente_actual).delete()
        
        return redirect('index:carrito')
    
    cliente_actual = cliente.objects.get(Id_cliente=2)  # Obtener el cliente actual (puedes cambiar el ID según tus necesidades)
    carrito_productos = carrito.objects.filter(Id_cliente=cliente_actual)  # Obtener los productos del carrito del cliente actual
    
    total_carrito = sum(producto.Id_producto.Presio_P for producto in carrito_productos)  # Calcular el precio total del carrito
    
    context = {
        'productos_carrito': carrito_productos,
        'total_carrito': total_carrito
    }
    return render(request, 'carrito.html', context)

def inicio(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            contraseña = form.cleaned_data['contraseña']
            cliente_obj = cliente.objects.filter(Correo=correo).first()
            print("Contraseña ingresada:", contraseña)
            print("Contraseña almacenada:", cliente_obj.Contraseña)
            print
            if cliente_obj is not None and check_password(contraseña, cliente_obj.Contraseña):
                user = authenticate(request, username=cliente_obj.Correo, password=contraseña)
                if user is not None:
                    login(request, user)
                    # Inicio de sesión exitoso, redirige a la página "index:tienda"
                    return redirect('index:tienda')
            # Las credenciales no son válidas, muestra un mensaje de error
            messages.error(request, 'Correo o contraseña incorrectos.')
    else:
        form = LoginForm()
        
    return render(request, 'inico.html', {'form': form})
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Encriptar la contraseña antes de guardarla en la base de datos
            contraseña = form.cleaned_data['Contraseña']
            form.instance.Contraseña = make_password(contraseña)
            
            form.save()
            return redirect("index:home")  # Redirecciona a la página de inicio después del registro exitoso
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})
def tienda(request):
    Articulo = articulos.objects.all()
    context = {"Articulo": Articulo}
    return render(request, "TIENDA.HTML", context)

class RegistroForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['Nombre', 'Apellido', 'Correo', 'Contraseña', 'Edad']
        widgets = {
            'Contraseña': forms.PasswordInput()  # Para ocultar la contraseña
        }

    def clean_Edad(self):
        edad = self.cleaned_data.get('Edad')
        if edad is not None and edad < 18:
            raise forms.ValidationError("Debes ser mayor de 18 años.")
        return edad

    def clean_Correo(self):
        correo = self.cleaned_data.get('Correo')
        if correo and not correo.endswith(('@gmail.com', '@yahoo.com', '@hotmail.com', '@outlook.com')):
            raise forms.ValidationError("El correo debe ser de Gmail, Yahoo, Hotmail o Outlook.")
        return correo
    
def eliminar_producto(request, producto_id):
    if request.method == 'POST':
        try:
            producto = carrito.objects.get(pk=producto_id)
            producto.delete()
        except carrito.DoesNotExist:
            pass

    return redirect('index:carrito')