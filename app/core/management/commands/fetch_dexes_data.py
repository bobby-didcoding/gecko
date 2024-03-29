"""
Management utility for fetching dex data from Gecko Terminal.
"""

from django.core.management.base import BaseCommand
from apis.gecko_terminal.client import Client
from core.models import Dex, Network


class Command(BaseCommand):

    help = "Fetching dexes data from Gecko Terminal"
    requires_migrations_checks = True
    stealth_options = ("stdin",)

    def handle(self, *args, **options):
        networks = Network.objects.all()
        for network in networks:
            data = Client(network=network.external_id).get_dexes()
            if data:
                for dex in data:
                    obj, created = Dex.objects.get_or_create(**dex)
        return "Dexes updated"
