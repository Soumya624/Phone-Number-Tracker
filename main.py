from phonenumbers import carrier
import phonenumbers
from test import number

from phonenumbers import geocoder
country = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(country, "en"))

service = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service, "en"))
