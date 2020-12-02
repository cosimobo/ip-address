#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install global-land-mask


# In[7]:


pip install geopy


# In[ ]:


import random
import socket
import struct
socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))


# In[ ]:


import requests

url = "https://freegeoip.app/json/"

headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)


# In[ ]:


import requests
import pandas as pd
import numpy as np
import json
import random
import socket
import struct
from geopy.geocoders import Nominatim
import os
from global_land_mask import globe


# In[ ]:


#fa una lista di 100 ip address random


# In[ ]:


def getting_ip_address():
    new, explored=[],[]
    i=0
    while i<100:
        ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        if ip in explored:
            continue
        else:
            new.append(ip)
        i+=1
    new = pd.DataFrame(new, columns=['ip'])
    return new


# In[1]:


#questa funzione chiama l'API e ritorna la risposta


# In[ ]:


def getting_ip(row):
    url = f"https://freegeoip.app/json/{row}"       # getting records from getting ip address
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
        }
    response = requests.request("GET", url, headers=headers)
    respond = json.loads(response.text)
    return respond


# In[ ]:


getting_ip("79.50.186.51") #Metto il mio ip


# In[2]:


#L'output sopra è in formato JSON (JavaScript Object Notation)
#viene salvato come una colonna in pandas (?)
#la funzione sotto richiama API e aggiunge informazioni alla colonna di pandas 


# In[ ]:


def get_information():
    new = getting_ip_address()
    new['info'] = new['ip'].apply(lambda row: getting_ip(row))
    new['time_zone'] = new['info'].apply(lambda row: row['time_zone'])
    new['latitude'] = new['info'].apply(lambda row: row['latitude'])
    new['longitude'] = new['info'].apply(lambda row: row['longitude'])
    new['on_land'] = new.apply(lambda row: globe.is_land(row['latitude'],row['longitude']),axis=1)
    new = new[new['latitude']!=0]
    new = new[new['on_land']==True]
    new['address'] = new.apply(lambda row: getting_city_nominatim(row),axis=1)
    return new


# In[3]:


#Questa funzione chiama il geopy API e ritorna l'output json


# In[ ]:


def getting_city_nominatim(row):
    try:
        lat = row['latitude']
        lon = row['longitude']
        geolocator = Nominatim(user_agent="my-application")
        location = geolocator.reverse(f"""{lat,lon}""")
        address = location.raw['address']
        return address
    except:
        print('timeout')


# In[4]:


#adesso devo salvare sul CVS quindi faccio la funzione sotto che aggiunge i nuovi ip address al dataframe e mi assicuro che non si s


# In[ ]:


def append_to_existing_df(new):
    if os.path.isfile(f'{os.path.abspath("")}\location_of_ip_address.csv'):
        new.to_csv('location_of_ip_address.csv', mode='a', header=False,index=False)
    else:
        new.to_csv('location_of_ip_address.csv', mode='w', header=True,                   columns=['ip','info','time_zone','latitude','longitude','address'],index=False)

def deleting_duplicate_entries():
    df = pd.read_csv('location_of_ip_address.csv')
    df.sort_values('ip',inplace=True)
    df.drop_duplicates(subset='ip',keep='first',inplace=True)
    df.to_csv('location_of_ip_address.csv',index=False)


# In[5]:


#dopo che ho fatto run alla funzione seguente dovrebbe dare i seguenti risultati


# In[ ]:


def main():
    new = get_information()
    append_to_existing_df(new)
    deleting_duplicate_entries()
if __name__ == '__main__':
    main()

