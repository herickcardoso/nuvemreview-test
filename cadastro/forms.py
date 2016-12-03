# -*- coding: utf-8 -*-
from django import forms
from cadastro.models import Inscricao

class InscricaoForm(forms.ModelForm):

	class Meta:
		model = Inscricao
		fields = ('nome','valor','CPU','RAM','SO','Armazenamento')
