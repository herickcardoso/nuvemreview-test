# -*- coding: utf-8 -*-
from django.db import models


class Inscricao(models.Model):
    nome = models.CharField('Serviço', max_length=100)
    #link = models.CharField('link', max_length=200)
    valor = models.DecimalField('Valor $', max_digits=5, decimal_places=2)
    CPU = models.PositiveSmallIntegerField('CPU',)
    clockCPU =models.DecimalField('Clock', max_digits=5, decimal_places=2)
    RAM = models.DecimalField('RAM', max_digits=5, decimal_places=1)
    SO = models.CharField('S.O.', max_length=100)
    armazenamento = models.CharField('Armazenamento',max_length=100)
    scaleup = models.PositiveSmallIntegerField('Scale Up',)
    scaledown = models.PositiveSmallIntegerField ('Scale Down',)
    datacenters = models.PositiveSmallIntegerField('Datacenters',)
    #email = models.EmailField(unique=True)
    #telefone = models.CharField(max_length=20, blank=True)
    criado_em = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ['criado_em']
        verbose_name = (u'nome')
        verbose_name_plural = (u'nomes')

    def __unicode__(self):
        return self.nome

#    def _get_dobro_idade(self):
#    return self.idade * 2
#    dobro_idade = property(_get_dobro_idade)
