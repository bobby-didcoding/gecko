from django.db import models
from django.db.models.signals import post_save


class CustomPoolManager(models.Manager):
    def bulk_create(self, objs, **kwargs):
        qs = super(models.Manager, self).bulk_create(objs, **kwargs)
        for i in objs:
            post_save.send(i.__class__, instance=i, created=True)
        return qs
