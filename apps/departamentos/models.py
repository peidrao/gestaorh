from django.db import models

from apps.empresas.models import Empresa
# Create your models here.

class Departamento(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da empresa')
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.nome}'