from django.shortcuts import render,redirect
from .forms import UserForm

# Create your views here.

def crearUsuario(request):
    if request.method == 'POST':
        usuario_form = UserForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('landingPage')
    else:
        usuario_form = UserForm()
        print(usuario_form)
    return render(request,'registration/registro.html',{'usuario_form':usuario_form})