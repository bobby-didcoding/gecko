from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command
from apis.gecko_terminal.client import Client
from core.models import Token


logger = get_task_logger(__name__)


@shared_task(bind=True)
def fetch_network_data(self):
    call_command('fetch_network_data')


@shared_task(bind=True)
def fetch_trending_pools_data(self):
    call_command('fetch_trending_pools_data')


@shared_task(bind=True)
def fetch_token_data(self, **kwargs):

    network = kwargs.get("network")
    address = kwargs.get("address")

    data = Client(
        network=network,
        address=address
    ).get_token_info()
    if data:
        for token in data:
            obj = Token.objects.filter(external_id=address)
            obj.update(**token)
    return "Token updated"
