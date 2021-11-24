from django.shortcuts import redirect, render
from django.urls import reverse

from apps.empresas.models import Empresa
from .forms import EmpresaForm
from apps.funcionarios.models import Funcionario


def create(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            data = Empresa()
            data.nome = form.cleaned_data['nome']
            data.save()
            funcionario = Funcionario.objects.get(id=request.user.id)
            funcionario.empresa_id = data.id
            funcionario.save()

            return redirect(reverse('home'))

    context = {
        'form': EmpresaForm
    }
    return render(request, 'create_empresa.html', context)


def edit(request, id):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            empresa = Empresa.objects.get(id=id)
            empresa.nome = form.cleaned_data['nome']
            empresa.save()

            return redirect(reverse('home'))

    context = {
        'form': EmpresaForm
    }

    return render(request, 'edit_empresa.html', context)
