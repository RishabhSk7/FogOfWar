import folium
import json

with open("Uttarakhand.geojson", "r") as file:
    data = json.load(file)
    data = data["features"]

lat, lon = [], []
for x in data:
    for i in  x["geometry"]["coordinates"][0]:
        lat.append(i[0])
        lon.append(i[1])
    
lat = (max(lat)+min(lat))/2
lon = (max(lon)+min(lon))/2
print(lat, lon)

m = folium.Map(zoom_start=9, location=[lon, lat], tiles="Stamen Terrain")     #the values in geojson are [lon, lat] instead of lat, lon
folium.GeoJson("Uttarakhand.geojson").add_to(m)

lat, lon = [], []
for x in data:
    for i in  range(0, len(x["geometry"]["coordinates"][0]), 300):
        y = x["geometry"]["coordinates"][0][i]
        folium.raster_layers.ImageOverlay(
            image="hehe.png",
            bounds=[[y[1], y[0]],[y[1]+1, y[0]+1]],
            opacity=1,
            interactive=False,
            cross_origin=False,
            zindex=1,
            alt='cloud'
        ).add_to(m)

m.save("footprint.html")
