import urllib2
import json

def geolocation():
     f = urllib2.urlopen('http://freegeoip.net/json/')
     json_string = f.read()
     f.close()
     location = json.loads(json_string)
     return location

city = geolocation['city']
county = geolocation['region_name']
country = geolocation['country_name']
zip = geolocation['zipcode']
