from django.db import models

from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField(
        max_length=255, help_text='Descição do documento')
    funcionario = models.ForeignKey(
        Funcionario, on_delete=models.PROTECT, null=True, blank=True)
    documento = models.FileField(upload_to='documentos/')

    def __str__(self) -> str:
        return f'{self.descricao}'
