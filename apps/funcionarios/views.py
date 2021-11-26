from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from apps.funcionarios.models import Funcionario
from apps.funcionarios.forms import FuncionarioForm


def index(request):
    return HttpResponse('Hello World!')


def list(request):
    funcionarios = Funcionario.objects.filter(empresa=request.user.empresa, is_active=True)

    context = {'funcionarios': funcionarios}

    return render(request, 'list.html', context)


def add(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('home'))

    context = {
        'form': FuncionarioForm,
    }

    return render(request, 'add.html', context)


@csrf_exempt
def delete(request):
    if request.method == 'POST':
        id_funcionario = request.POST['id_funcionario']
        try:
            funcionario = Funcionario.objects.get(id=id_funcionario)
            funcionario.is_active = False
            funcionario.save()
            response = {'icon': 'success', 'title': 'Sucesso',
                        'text': 'Funcionário removido com sucesso!'}
        except Funcionario.DoesNotExist:
            response = {'icon': 'error', 'title': 'Erro',
                        'text': 'Não foi encontrado o funcionário'}

        return JsonResponse(response, safe=False)


def edit(request, id):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            funcionario = Funcionario.objects.get(id=id)
            funcionario.username = form.cleaned_data['username']

            funcionario.set_password(form.cleaned_data['password'])
            funcionario.first_name = form.cleaned_data['first_name']
            funcionario.last_name = form.cleaned_data['last_name']
            funcionario.email = form.cleaned_data['email']
            funcionario.last_name = form.cleaned_data['last_name']
            funcionario.departamentos.set(form.cleaned_data['departamentos'])
            funcionario.empresa = form.cleaned_data['empresa']
            funcionario.is_active = form.cleaned_data['is_active']
            funcionario.is_superuser = form.cleaned_data['is_superuser']
            funcionario.is_staff = form.cleaned_data['is_staff']

            funcionario.save()

            return redirect(reverse('home'))

    form = FuncionarioForm()

    context = {
        'form': form
    }

    return render(request, 'edit.html', context)
