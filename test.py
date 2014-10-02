from geoLocation import geoLocation

myLocation = geoLocation()
ip = myLocation['city']
country_code = myLocation['country_code']
county_code = myLocation['region_code']
latitude = myLocation['latitude']
longitude = myLocation['longitude']
metro_code = myLocation['metro_code']
area_code = myLocation['area_code']
city = myLocation['city']
county = myLocation['region_name']
country = myLocation['country_name']
zip = myLocation['zipcode']
