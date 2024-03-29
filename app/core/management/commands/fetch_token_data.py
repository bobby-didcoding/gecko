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
        for token in Token.objects.all():
            data = Client(
                network=token.network.external_id,
                address=token.external_id
            ).get_token_info()
            if data:
                for token in data:
                    obj = Token.objects.filter(external_id=token.external_id)
                    obj.update(**token)
            return "Tokens updated"