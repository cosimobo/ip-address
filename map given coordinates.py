# https://towardsdatascience.com/easy-steps-to-plot-geographic-data-on-a-map-python-11217859a2db

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("location_of_ip_address.csv")

df.head()



















"""
import requests
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



CSV_URL = "https://freegeoip.app/json"


with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    df = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(df)
    for row in my_list:
        print(row)







url = "https://freegeoip.app/json"
response = requests.get(url)

#check
if response.status_code != 200:
    print("Failed to get data:", response.status_code)
else:
    print("First 250 characters of data are")
    print(response.text[:250])

#now we can see the latitude and longitude

print(response.content)

df = csv.reader(response, dialect=csv)
for row in df:
    print(row)



df = pd.read_csv("https://freegeoip.app/json")

df.head()

BBox = ((df.longitude.min(),   df.longitude.max(),
         df.latitude.min(), df.latitude.max()))

BBox

# opestreetmap.org https://medium.com/@abuqassim115/thanks-for-your-response-frank-fb869824ede2

ruh_m = plt.imread('C:/.. … /Riyadh_map.png')

fig, ax = plt.subplots(figsize=(8, 7))
ax.scatter(df.longitude, df.latitude, zorder=1, alpha=0.2, c='b', s=10)
ax.set_title('Plotting Spatial Data on Riyadh Map')
ax.set_xlim(BBox[0], BBox[1])
ax.set_ylim(BBox[2], BBox[3])
ax.imshow(ruh_m, zorder=0, extent=BBox, aspect='equal')
"""
