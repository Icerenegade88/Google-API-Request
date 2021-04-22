import urllib3
import urllib.parse
main_api = 'https://maps.googleapis.com/maps/api/geocode/json?'
class build_url:
    def __init__(self, address, key):
        self.address = address
        self.key = key
            
    def full_url(self):
        url = main_api + urllib.parse.urlencode({'address': self.address, 'key' : self.key})
        return url

api_key = input("Enter your API key: ")
addy_in = input("Enter the Address you want to query: ")
first_url = build_url(addy_in, api_key)