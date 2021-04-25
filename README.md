#Google-API-Request
Learning how to interact with Google API

This may help newcomers out with understanding the interaction between python and Google API, this is also my learning process that might help you.

## What does main.py do? 
main.py is a script/program that uses Google's Geocoding API to let the user request addresses in JSON format that is then parsed and searched for the full address, and LAT,LNG coordinates to use in another program or in one of Google's other API's such as Google Maps.


## What is build_url.py?

### Code
```python
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
```
build_url.py is a module I built for myself to try to make the url building process cleaner and to help you build a simple URL

## How to use the module:
```python
#When you download this github project it will already be imported into main.py but if you want to use it in your own program, make sure it's in the same folder then:
import build_url

#using the module:

url = build_url.first_url.full_url() #this will create your full url when it is called
print(url) #will print it there will be more added in the future
```

## What is the testcode folder?
The test code folder is to test code ive been working on that is unfinished or un-used
