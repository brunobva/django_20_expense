from django.forms import ModelForm
from . import models
from .models import Transacao

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'categoria', 'valor', 'observacao']