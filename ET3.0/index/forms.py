from django import forms
from .models import cliente
from django.contrib.auth.forms import AuthenticationForm

class RegistroForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['Nombre', 'Apellido', 'Correo', 'Contraseña', 'Edad']
        widgets = {
            'Contraseña': forms.PasswordInput()  # Para ocultar la contraseña
        }

class LoginForm(AuthenticationForm):
    correo = forms.EmailField(label='Correo electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)