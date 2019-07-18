from django.core.management.base import BaseCommand
from catalogueapp.models import Organisation, Service
from catalogueapp.tools import ALISS_Importer


class Command(BaseCommand):
    help = 'Update ALISS Data'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        importer = ALISS_Importer()
        for organisation in Organisation.objects.all():
            importer.update_organisation(organisation)
        for service in Service.objects.all():
            importer.update_service(service)
