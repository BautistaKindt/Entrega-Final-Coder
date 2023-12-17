from django.shortcuts import render, redirect
from django.http import HttpResponse
from FinalApp.models import Usuario
from FinalApp.forms import UserForm, User_Formulario, UserEditForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm




def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})



def inicio(request):
    contexto = {}
    return HttpResponse(request, 'templates', contexto)

def crear_user_form(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            informacion = user_form.cleaned_data
            user_create = Usuario(
                username=informacion["username"],
                email=informacion["email"],
                first_name=informacion["first_name"],
                last_name=informacion["last_name"],
                imagen_avatar=informacion.get("imagen_avatar"),
                password=informacion["password1"],
            )
            user_create.save()

            login(request, user_create)

            return redirect("FinalApp/inicio")

    user_form = UserForm()
    contexto = {"form": user_form}
    return render(request, "FinalApp/create_user_form.html", contexto)


def usuario(request):
      if request.method == 'POST':
            miFormulario = User_Formulario(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  usuario = Usuario(nombre=informacion['curso'])
                  usuario.save()
                  return render(request, "FinalApp/inicio.html")
      else:

            miFormulario = User_Formulario()

      return render(request, "FinalApp/inicio.html", {"miFormulario":miFormulario})


def buscar(request):
    if request.GET["usuario"]:
        usuario = request.GET['usuario']
        return render(request, "FinalApp/inicio.html", {"usuario": usuario})
    else:
        respuesta = "No enviaste datos"
    return render(request, "FinalApp/inicio.html", {"respuesta": respuesta})


def logout_request(request):
    logout(request)

    return redirect("inicio")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "FinalApp/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:

                return render(request, "FinalApp/inicio.html", {"mensaje": "Error, datos incorrectos"})

        else:

            return render(request, "FinalApp/inicio.html", {"mensaje": "Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "accounts/login.html", {'form': form})


@login_required
def editarPerfil(request):
    # Instancia del login
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()

            return render(request, "FinalApp/inicio.html")  # Vuelvo al inicio o a donde quieran

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "accounts/editarperfil.html", {"miFormulario": miFormulario, "usuario": usuario})








