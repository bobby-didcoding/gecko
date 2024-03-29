from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Pool, Network, Dex, Token, TokenPair
from tasks.tasks import fetch_token_data


@receiver(post_save, sender=Pool, weak=False)
def create_pool(sender, instance, created, **kwargs):
    if created:
        '''
        Process foreign keys
        '''
        network = Network.objects.get(
            external_id = instance.relationships["network"]["data"]["id"],
            type = "network"
        )

        dex, created = Dex.objects.get_or_create(
            external_id = instance.relationships["dex"]["data"]["id"],
            network = network,
            type = "dex"
        )

        base_token, created = Token.objects.get_or_create(
            external_id = instance.relationships["base_token"]["data"]["id"],
            dex=dex,
            network=network,
            type = "token"
        )

        quote_token, created = Token.objects.get_or_create(
            external_id = instance.relationships["quote_token"]["data"]["id"],
            dex=dex,
            network=network,
            type = "token"
        )

        token_pair, created = TokenPair.objects.get_or_create(
            base_token = base_token,
            quote_token = quote_token
        )

        instance.network = network
        instance.dex = dex
        instance.token_pair = token_pair
        instance.save()

        
@receiver(post_save, sender=Token, weak=False)
def create_token(sender, instance, created, **kwargs):
    if created:
        '''
        Fetch token attributes
        '''
        fetch_token_data.delay(
            network = instance.network.external_id,
            address = instance.external_id
        )
