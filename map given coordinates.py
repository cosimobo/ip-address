
# https://towardsdatascience.com/easy-steps-to-plot-geographic-data-on-a-map-python-11217859a2db

import pandas as pd
import matplotlib.pyplot as plt

csv_file= ("location_of_ip_address.csv")
df = pd.read_csv(csv_file)

df.head()

BBox = ((df.longitude.min(),   df.longitude.max(),
         df.latitude.min(), df.latitude.max()))

print(BBox)
# (-122.9638, 151.1021, -37.6363, 55.7028)

mymap = plt.imread("map.png")

#plot df.longitude and df.latitude coordinates as scatter points on the mymap map image

fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(df.longitude, df.latitude, zorder=1, alpha= 0.2, c='b', s=10)
ax.set_title('Plotting Spatial Data on Riyadh Map')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(mymap, zorder=0, extent = BBox, aspect= 'equal')
