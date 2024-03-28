"""
Management utility for fetching network data from Gecko Terminal.
"""
from django.core.management.base import BaseCommand
from apis.gecko_terminal.client import Client
from core.models import Network

class Command(BaseCommand):
    
    help = "Fetching network data from Gecko Terminal"
    requires_migrations_checks = True
    stealth_options = ("stdin",)

    def handle(self, *args, **options):
        data = Client().get_networks()
        if data:
            for network in data:
                obj, created = Network.objects.get_or_create(**network)
        return "Networks updated"