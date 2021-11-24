from django import forms

from .models import Funcionario


class FuncionarioForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = (
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "departamentos",
            "empresa",
            "is_active",
            "is_superuser",
            "is_staff",
        )