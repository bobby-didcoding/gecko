import os
from django.db import models
import uuid
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
)
from .managers import CustomPoolManager


class BaseModel(models.Model):
    class Meta:
        abstract = True
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    external_id = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    attributes = models.JSONField(blank=True, null=True)
    relationships = models.JSONField(blank=True, null=True)
    

class Network(
    TimeStampedModel,
    ActivatorModel,
    BaseModel
):

    class Meta:
        verbose_name = "Network"
        verbose_name_plural = "Networks"
        ordering = ['id']
    

class Dex(
    TimeStampedModel,
    ActivatorModel,
    BaseModel
):

    class Meta:
        verbose_name = "Dex"
        verbose_name_plural = "Dexes"
        ordering = ['id']


class Token(
    TimeStampedModel,
    ActivatorModel,
    BaseModel
):

    class Meta:
        verbose_name = "Token"
        verbose_name_plural = "Tokens"
        ordering = ['id']


class Pool(
    TimeStampedModel,
    ActivatorModel,
    BaseModel
):

    class Meta:
        verbose_name = "Pool"
        verbose_name_plural = "Pools"
        ordering = ['id']

    objects = CustomPoolManager()

    base_token = models.ForeignKey(Token, related_name="pool_base_token", blank=True, null=True, on_delete=models.SET_NULL)
    quote_token = models.ForeignKey(Token, related_name="pool_quote_token", blank=True, null=True, on_delete=models.SET_NULL)
    network = models.ForeignKey(Network, related_name="pool_network", blank=True, null=True, on_delete=models.SET_NULL)
    dex = models.ForeignKey(Dex, related_name="pool_dex", blank=True, null=True, on_delete=models.SET_NULL)

    @property
    def todo(self):
        return f'{self.external_id} - playing'
