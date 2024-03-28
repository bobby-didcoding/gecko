from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Pool, Network, Dex, Token


@receiver(post_save, sender=Pool, weak=False)
def create_customer(sender, instance, created, **kwargs):
    if created:
        '''
        Process foreign keys
        '''
        dex, created = Dex.objects.get_or_create(name = instance["relationships"]["dex"]["data"]["id"])
        network, created = Network.objects.get_or_create(name = instance["relationships"]["network"]["data"]["id"])
        base_token, created = Token.objects.get_or_create(name = instance["relationships"]["base_token"]["data"]["id"])
        quote_token, created = Token.objects.get_or_create(name = instance["relationships"]["quote_token"]["data"]["id"])

        