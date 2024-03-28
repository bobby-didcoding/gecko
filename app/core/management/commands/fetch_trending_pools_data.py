"""
Management utility for fetching trending pools from Gecko Terminal.
"""
from django.core.management.base import BaseCommand
from apis.gecko_terminal.client import Client
from core.models import Pool

class Command(BaseCommand):
    
    help = "Fetching trending pools from Gecko Terminal"
    requires_migrations_checks = True
    stealth_options = ("stdin",)

    def handle(self, *args, **options):
        pools = [Pool(**p) for p in Client().get_trending_pools()]
        if pools:
            Pool.objects.all().delete()
            Pool.objects.bulk_create(pools)
        return "Pools updated"