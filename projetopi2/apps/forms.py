from django import forms

from .models import LoginPrestador, Login

class LoginPrestadorForm(forms.ModelForm):
    class Meta:
        model = LoginPrestador
        fields = ('nome','telefone','email','senha','cep','numero',
        'complemento','profissional')
