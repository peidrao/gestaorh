from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Departamento
from .forms import DepartamentoForm


def list(request):
    departamentos = Departamento.objects.filter(
        empresa=request.user.empresa, is_active=True)
    context = {'departamentos': departamentos}

    return render(request, 'list_departamentos.html', context)


def create(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            Departamento.objects.create(
                nome=form.cleaned_data['nome'],
                is_active=form.cleaned_data['is_active'],
                empresa=request.user.empresa
            )
            return redirect(reverse('departamento:list'))
        else:
            return redirect(reverse('departamento:create'))

    context = {
        'form': DepartamentoForm
    }

    return render(request, 'create_departamento.html', context)


def update(request, id):
    departamento = Departamento.objects.get(id=id)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            departamento.nome = form.cleaned_data['nome']
            departamento.is_active = form.cleaned_data['is_active']
            departamento.save()
            return redirect(reverse('departamento:list'))
        else:
            return redirect(reverse('departamento:update'))
            

    context = {
        'form': DepartamentoForm,
        'departamento': departamento
    }

    return render(request, 'update_departamento.html', context)

@csrf_exempt
def delete(request):
    if request.method == 'POST':
        id_departamento = request.POST['id_departamento']
        try: 
            departamento = Departamento.objects.get(id=id_departamento)
            departamento.is_active = False
            departamento.save()
            response = {'icon': 'success', 'title': 'Sucesso', 'text': 'Departamento removido com sucesso!'}
        except Departamento.DoesNotExist:
            response = {'icon': 'error', 'title': 'Erro', 'text': 'Não foi encontrado o departamento!'}

        return JsonResponse(response, safe=False)