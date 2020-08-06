import folium
import pandas
data=pandas.read_csv("csv1.csv")
name=list(data["City_name"])
lat=list(data["lat"])
lon=list(data["lon"])
color=list(data["color"])
map = folium.Map(location=(12.58,77.48),zoom_start=6)
fg = folium.FeatureGroup(name="Banglore map")
for name,lt,ll,clr in zip(name,lat,lon,color):
    fg.add_child(folium.Marker(location=(lt,ll), popup=name, icon=folium.Icon(color=clr)))
map.add_child(fg)
map.save('hwmap1.html')