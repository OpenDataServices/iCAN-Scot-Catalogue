from django.db import models


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
