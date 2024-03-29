"""
Management utility for fetching token data from Gecko Terminal.
"""
from django.core.management.base import BaseCommand
from apis.gecko_terminal.client import Client
from core.models import Token

class Command(BaseCommand):
    
    help = "Fetching token data from Gecko Terminal"
    requires_migrations_checks = True
    stealth_options = ("stdin",)

    def handle(self, *args, **options):
        '''
        This needs more work!
        Need to use the multiple endpoint to avoid rate limits
        '''
        for token in Token.objects.all():
            data = Client(
                network=token.network.external_id,
                address=token.external_id.split("_")[1]
            ).get_token_info()
            if data:
                obj = Token.objects.filter(external_id=data["external_id"])
                obj.update(**data)
        return "Tokens updated"