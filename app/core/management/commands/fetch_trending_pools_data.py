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
        data = Client().get_trending_pools()
        if data:
            for pool in data:
                obj, created = Pool.objects.get_or_create(**pool)
        return "Pools updated"
