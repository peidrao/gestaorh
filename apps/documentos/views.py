from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Documento
from .forms import DocumentoForm



def create(request, id):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)

        if form.is_valid():
            Documento.objects.create(
                descricao=form.cleaned_data['descricao'],
                documento=form.cleaned_data['documento'],
                funcionario_id=id
            )

            return redirect(reverse('funcionario:list'))
        else:
            return redirect(reverse('documento:create', id))

    context = {
        'form': DocumentoForm
    }

    return render(request, 'create_documento.html', context)


def list(request, id):
    context = {}
    try:
        documentos = Documento.objects.filter(funcionario_id=id)
        context['documentos'] = documentos
    except Documento.DoesNotExist:
        return redirect(reverse('funcionario:list'))
    return render(request, 'view_documento.html', context)