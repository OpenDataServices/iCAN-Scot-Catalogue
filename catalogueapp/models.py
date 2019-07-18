from django.db import models
import json


class CatalogueAdminPermission(models.Model):
    class Meta:
        managed = False
        permissions = (
            ('catalogueadmin', 'Can Admin The Catalogue'),
        )


class Organisation(models.Model):
    aliss_id = models.UUIDField(unique=True, blank=False)
    name = models.TextField(blank=True)
    aliss_url = models.URLField(blank=True)
    aliss_permalink = models.URLField(blank=True)
    slug = models.TextField(blank=True)
    description = models.TextField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    url = models.URLField(blank=True)
    phone = models.TextField(blank=True)
    email = models.EmailField(blank=True)


class Service(models.Model):
    aliss_id = models.UUIDField(unique=True, blank=False)
    organisation = models.ForeignKey(
        'Organisation',
        on_delete=models.PROTECT,
    )
    slug = models.TextField(blank=True)
    aliss_url = models.URLField(blank=True)
    aliss_permalink = models.URLField(blank=True)
    name = models.TextField(blank=True)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    phone = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    active = models.BooleanField(blank=False)


class ALISSMeta(models.Model):
    # attribution is actually a JSON block.
    # But we don't need to do any database operations within that JSON, so we'll leave it as TextField for maximum DB compatibility. # noqa
    attribution = models.TextField(blank=True)
    licence = models.TextField(blank=True)

    def get_attribution_list(self):
        if self.attribution:
            return json.loads(self.attribution)
        else:
            return []
