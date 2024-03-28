from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command

logger = get_task_logger(__name__)


@shared_task(bind=True)
def get_token_data(self):

    call_command('fetch_trending_pools')

    print("test")
    pass
