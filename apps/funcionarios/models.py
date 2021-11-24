from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(AbstractUser):
    departamentos = models.ManyToManyField(Departamento, blank=True)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.SET_NULL, null=True, blank=True)

    def set_password(self, password):
        return super().set_password(password)

    def __str__(self) -> str:
        return f'{self.username}'
