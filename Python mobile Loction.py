import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

number = input("enter your Mobile number with Country Start with + : ")

Num_loc = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(Num_loc,"en"))

service_name = phonenumbers.parse(number,"RO")

print(carrier.name_for_number(service_name,"en"))
