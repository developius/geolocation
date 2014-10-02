import urllib2
import json

def geoLocation():
     f = urllib2.urlopen('http://freegeoip.net/json/')
     json_string = f.read()
     f.close()
     location = json.loads(json_string)
     return location
