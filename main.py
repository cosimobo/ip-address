import requests
import json


IP_URL ='http://ip-api.com/json/{}'

def parse_arguments():
    parser=argparse.ArgumentParser(
            description="IP ADDRESS prject")
    parser.add_argument ("ip_address", type=str,
                         help= "Insert an IP Address",
                         default=None)
    parser.add_argument('-u', help="username name (requires -p)",
                         default=None)
    parser.add_argument('-p', help="username password",
                         default=None)

#import hashlib
#import random
#password = "the password typed by the user "
#salt = str ( random . random () )
#concat = salt + password
#digest = hashlib . sha256 ( concat . encode (’utf -8’) ). hexdigest ()
#print ( digest )
#> 52793290377fd8e5038e140b0b60e266a6b9fb26ce2980a2aace83f2d257df2c

def get_location(ip_address):

    URL = IP_URL.format(ip_address)
    r = requests.get(URL)
    info = json.loads(r.text)
    #print(info)
    try:
        location = info['country']
        city = info['city']
    except KeyError:
        print('Error')

    return location, city

from ip_address import get_location

ip_address = '153.138.24.18'

country, city = get_location(ip_address)

print("IP address {} is from {}, {} ".format(ip_address, city,  country))
