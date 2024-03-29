from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command


logger = get_task_logger(__name__)


@shared_task(bind=True)
def fetch_network_data(self):
    call_command("fetch_network_data")


@shared_task(bind=True)
def fetch_trending_pools_data(self):
    call_command("fetch_trending_pools_data")


@shared_task(bind=True)
def fetch_token_data(self, **kwargs):
    call_command("fetch_token_data")
