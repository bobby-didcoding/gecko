import os
from django.db import models
import uuid
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
)


def team_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/policies/<slug>/<filename>
    return os.path.join('team', str(instance.name), filename)


class Pool(
    TimeStampedModel,
    ActivatorModel,
    models.Model
):

    class Meta:
        verbose_name = "Pool"
        verbose_name_plural = "Pools"
        ordering = ['id']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    external_id = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    attributes = models.JSONField()
    relationships = models.JSONField()
