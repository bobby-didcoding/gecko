from __future__ import absolute_import, unicode_literals
import os
from datetime import timedelta
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
app = Celery("demo")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "fetch_trending_pools_data": {
        "task": "tasks.tasks.fetch_trending_pools_data",
        "schedule": timedelta(seconds=30),
    },
    "fetch_token_data": {
        "task": "tasks.tasks.fetch_token_data",
        "schedule": timedelta(seconds=30),
    },
}

app.autodiscover_tasks()
