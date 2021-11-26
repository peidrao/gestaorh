from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from apps.funcionarios.models import Funcionario

from .forms import RegistroHoraExtraForm
from .models import RegistroHoraExtra


def list(request, id):
    context = {}
    horas = RegistroHoraExtra.objects.filter(funcionario_id=id)
    funcionario = Funcionario.objects.get(id=id)
    context['funcionario'] = funcionario
    if horas:
        context['horas'] = horas
        
    else:
        context['sem_horas'] = True
    
    return render(request, 'list_horas.html', context)
        


def create(request, id):
    if request.method == 'POST':
        form = RegistroHoraExtraForm(request.POST)
        if form.is_valid():
            hora = RegistroHoraExtra.objects.create(
                motivo=form.cleaned_data['motivo'],
                horas=form.cleaned_data['horas'],
            )
            hora.funcionario_id = id
            hora.save()

            return redirect(reverse('funcionario:list'))
        else:
            return redirect(reverse('funcionario:list'))
    
    context = {
        'form': RegistroHoraExtraForm
    }
    return render(request, 'create_horas.html', context)


@csrf_exempt
def delete(request):
    if request.method == 'POST':
        id_hora = request.POST['id_hora']
        try: 
            RegistroHoraExtra.objects.get(id=id_hora).delete()
            response = {'icon': 'success', 'title': 'Sucesso', 'text': 'Funcionário removido com sucesso!'}
        except Funcionario.DoesNotExist:
            response = {'icon': 'error', 'title': 'Erro', 'text': 'Não foi encontrado o funcionário'}

        return JsonResponse(response, safe=False)

def edit(request, id):
    if request.method == 'POST':
        form = RegistroHoraExtraForm(request.POST)
        if form.is_valid():
            horas = RegistroHoraExtra.objects.get(id=id)
            horas.horas = form.cleaned_data['horas']
            horas.motivo = form.cleaned_data['motivo']
            horas.save()

            return redirect(reverse('funcionario:list'))

    context = {
        'form': RegistroHoraExtraForm()
    }

    return render(request, 'edit_horas.html', context)