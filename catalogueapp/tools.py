import requests
from catalogueapp.models import Service, Organisation, ALISSMeta
import json


class ALISS_URL:
    def __init__(self, url):
        self.url = url
        self.url_bits = url.split('/')

    def is_service(self):
        return self.url.startswith('https://www.aliss.org/services/')

    def get_service_api_url(self):
        if self.is_service():
            return 'https://www.aliss.org/api/v4/services/' + self.url_bits[4]


class ALISS_Importer:
    def __init__(self):
        pass

    def import_from_service_URL(self, url):
        response = requests.get(url.get_service_api_url())
        response.raise_for_status()
        data = response.json()
        try:
            service = Service.objects.get(aliss_id=data['data']['id'])
        except Service.DoesNotExist:
            service = Service()
            service.aliss_id = data['data']['id']
            service.active = True
        self._process_service_data(service, data)
        return service

    def update_service(self, service):
        response = requests.get('https://www.aliss.org/api/v4/services/' + str(service.aliss_id))
        response.raise_for_status()
        data = response.json()
        self._process_service_data(service, data)
        self._process_meta(data)

    def update_organisation(self, organisation):
        response = requests.get('https://www.aliss.org/api/v4/organisations/' + str(organisation.aliss_id))
        response.raise_for_status()
        data = response.json()
        self._process_organisation_data(organisation, data)
        self._process_meta(data)

    def _process_service_data(self, service, data):
        # service details
        service.name = data['data']['name']
        service.aliss_url = data['data']['aliss_url']
        service.aliss_permalink = data['data']['permalink']
        service.slug = data['data']['slug']
        service.description = data['data']['description']
        service.url = data['data']['url']
        service.phone = data['data']['phone']
        service.email = data['data']['email']

        # organisation
        try:
            organisation = Organisation.objects.get(aliss_id=data['data']['organisation']['id'])
        except Organisation.DoesNotExist:
            organisation = Organisation()
            organisation.aliss_id = data['data']['organisation']['id']

        organisation.name = data['data']['organisation']['name']
        organisation.aliss_url = data['data']['organisation']['aliss_url']
        organisation.slug = data['data']['organisation']['slug']

        organisation.save()

        service.organisation = organisation

        # finally, save
        service.save()

    def _process_organisation_data(self, organisation, data):
        # organisation details
        organisation.name = data['data']['name']
        organisation.aliss_url = data['data']['aliss_url']
        organisation.aliss_permalink = data['data']['permalink']
        organisation.slug = data['data']['slug']
        organisation.description = data['data']['description']
        organisation.facebook = data['data']['facebook']
        organisation.twitter = data['data']['twitter']
        organisation.url = data['data']['url']
        organisation.phone = data['data']['phone']
        organisation.email = data['data']['email']

        # finally, save
        organisation.save()

    def _process_meta(self, data):
        try:
            meta = ALISSMeta.objects.get()
        except ALISSMeta.DoesNotExist:
            meta = ALISSMeta()

        meta.licence = data['meta']['licence']
        meta.attribution = json.dumps(data['meta']['attribution'])
        meta.save()
