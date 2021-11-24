from django.shortcuts import render
from .models import Departamento


def list(request):
    departamentos = Departamento.objects.filter(
        empresa=request.user.empresa, is_active=True)
    context = {'departamentos': departamentos}

    return render(request, 'list_departamentos.html', context)
