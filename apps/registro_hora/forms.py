from django import forms

from .models import RegistroHoraExtra


class RegistroHoraExtraForm(forms.ModelForm):

    class Meta:
        model = RegistroHoraExtra
        exclude = ('funcionario',)