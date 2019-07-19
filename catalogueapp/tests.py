from catalogueapp.tools import ALISS_URL


def test_aliss_url_is_service_1():
    assert ALISS_URL('https://www.aliss.org/services/elderflowers-0/').is_service()


def test_aliss_url_is_service_2():
    assert not ALISS_URL('https://www.aliss.org/organisations/hearts-and-minds-limited-0/').is_service()


def test_aliss_url_is_service_3():
    assert not ALISS_URL('http://opendataservices.coop/').is_service()
