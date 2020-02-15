import requests


def get_spn_object(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)
    json = response.json()
    envelope = json["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]['boundedBy']['Envelope']
    low = envelope['lowerCorner'].split()
    upp = envelope['upperCorner'].split()
    return f"{abs(float(upp[0]) - float(low[0])) / 2},{abs(float(upp[1]) - float(low[1])) / 2}"

