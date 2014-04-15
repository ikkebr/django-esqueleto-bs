from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, "base/index.html", {})

@login_required
def perfil(request):
    return render(request, "base/perfil.html", {})


def cadastro(request):
    if request.user.is_authenticated():
        return redirect("perfil")
    
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        usuario = form.save()
        messages.success(request, 'Cadastro realizado com sucesso.')
        return redirect(perfil)

    return render(request, "base/criar.html", {"form": form})
