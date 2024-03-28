from __future__ import absolute_import, unicode_literals
import os
from datetime import timedelta
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
app = Celery("demo")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "fetch_network_data": {
        "task": "tasks.tasks.fetch_network_data",
        "schedule": timedelta(minutes=2),
    },
    "fetch_dexes_data": {
        "task": "tasks.tasks.fetch_dexes_data",
        "schedule": timedelta(minutes=2),
    },
    "fetch_trending_pools_data": {
        "task": "tasks.tasks.fetch_trending_pools_data",
        "schedule": timedelta(minutes=2),
    },
}

app.autodiscover_tasks()
