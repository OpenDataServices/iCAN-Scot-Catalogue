import requests
from catalogueapp.models import Service, Organisation

class ALISS_URL:
    def __init__(self, url):
        self.url = url
        self.url_bits = url.split('/')

    def is_service(self):
        #TODO
        return True

    def get_service_api_url(self):
        if self.is_service():
            return 'https://www.aliss.org/api/v4/services/' + self.url_bits[4]


class ALISS_Importer:
    def __init__(self):
        pass

    def import_from_service_URL(self, url):
        response = requests.get(url.get_service_api_url())
        response.raise_for_status()
        return self._process_service_data(response.json())

    def _process_service_data(self, data):
        try:
            service = Service.objects.get(aliss_id=data['data']['id'])
        except Service.DoesNotExist:
            service = Service()
            service.aliss_id = data['data']['id']
            service.active = True

        service.name = data['data']['name']
        service.aliss_url = data['data']['aliss_url']
        service.aliss_permalink = data['data']['permalink']
        service.slug = data['data']['slug']
        service.description = data['data']['description']
        service.url = data['data']['url']
        service.phone = data['data']['phone']
        service.email = data['data']['email']
        service.organisation = self._process_organisation_data_in_service_object(data['data']['organisation'])

        service.save()

        return service

    def _process_organisation_data_in_service_object(self, data):
        try:
            organisation = Organisation.objects.get(aliss_id=data['id'])
        except Organisation.DoesNotExist:
            organisation = Organisation()
            organisation.aliss_id = data['id']

        organisation.name = data['name']
        organisation.aliss_url = data['aliss_url']
        organisation.slug = data['slug']

        organisation.save()

        return organisation
