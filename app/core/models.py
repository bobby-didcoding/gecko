from django.db import models
import uuid
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
)
from .managers import CustomPoolManager


class BaseModel(
    TimeStampedModel,
    ActivatorModel,
    models.Model
):
    class Meta:
        abstract = True
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    external_id = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    attributes = models.JSONField(blank=True, null=True)
    relationships = models.JSONField(blank=True, null=True)
    

class Network(BaseModel):

    class Meta:
        ordering = ['external_id']
    

class Dex(BaseModel):

    class Meta:
        verbose_name_plural = "Dexes"
        ordering = ['external_id']

    network = models.ForeignKey(Network, related_name="dex_network", on_delete=models.CASCADE)


class Token(BaseModel):

    class Meta:
        ordering = ['external_id']
    
    network = models.ForeignKey(Network, related_name="token_network", on_delete=models.CASCADE)
    dex = models.ForeignKey(Dex, related_name="token_dex", on_delete=models.CASCADE)

    @property
    def name(self):
        try:
            return self.attributes["name"]
        except (KeyError, TypeError):
            return "TBC"
    
    @property
    def address(self):
        try:
            return self.attributes["address"]
        except (KeyError, TypeError):
            return "TBC"
    
    @property
    def symbol(self):
        try:
            return self.attributes["symbol"]
        except (KeyError, TypeError):
            return "TBC"


class TokenPair(BaseModel):

    class Meta:
        ordering = ['external_id']

    base_token = models.ForeignKey(Token, related_name="token_pair_base_token", blank=True, null=True, on_delete=models.SET_NULL)
    quote_token = models.ForeignKey(Token, related_name="token_pair_quote_token", blank=True, null=True, on_delete=models.SET_NULL)


class Pool(BaseModel):

    class Meta:
        ordering = ['external_id']

    objects = CustomPoolManager()

    token_pair = models.ForeignKey(TokenPair, related_name="pool_base_token_pair", blank=True, null=True, on_delete=models.SET_NULL)
    network = models.ForeignKey(Network, related_name="pool_network", blank=True, null=True, on_delete=models.SET_NULL)
    dex = models.ForeignKey(Dex, related_name="pool_dex", blank=True, null=True, on_delete=models.SET_NULL)

    @property
    def name(self):
        return self.attributes["name"]
    
    @property
    def address(self):
        return self.attributes["address"]
    
    @property
    def base_token_price_usd(self):
        return self.attributes["base_token_price_usd"]
    
    @property
    def quote_token_price_usd(self):
        return self.attributes["quote_token_price_usd"]
    
    @property
    def base_token_price_quote_token(self):
        return self.attributes["base_token_price_quote_token"]
    
    @property
    def quote_token_price_base_token(self):
        return self.attributes["quote_token_price_base_token"]
