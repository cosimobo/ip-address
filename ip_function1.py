import json
import urllib
import urllib.request

def get_location():
    url = 'http://ip-api.com/json/{}'
    ip_address = "1.2.3.4"
    url = url.format(ip_address)
    json_obj = urllib.request.urlopen((url))
    js = json.load(json_obj)

    return js["city"], js["country"]

