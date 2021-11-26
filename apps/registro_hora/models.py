from django.db import models

from apps.funcionarios.models import Funcionario


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(
        max_length=255)
    funcionario = models.ForeignKey(
        Funcionario, on_delete=models.SET_NULL, null=True, blank=True)
    horas = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.motivo}'
