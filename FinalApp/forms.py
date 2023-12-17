from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class User_Formulario(UserCreationForm):
    nombre = forms.CharField()
    vlog = forms.CharField()
    imagen_avatar = forms.ImageField(required=False)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name', 'nombre', 'vlog', 'imagen_avatar']
        help_texts = {k: "" for k in fields}



class UserForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    imagen_avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k: "" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)