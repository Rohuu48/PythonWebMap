import folium
import pandas

data1=pandas.read_csv("restau-paris.csv")
data2=pandas.read_csv("paris.csv")
data3=pandas.read_csv("Volcanoes_USA.txt")


# mapping out volcanoes in USA and creating it's feature group

def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red'



#mapping out restaurants and tourist places in Paris
map= folium.Map(zoom_start=12, tiles="OpenStreetMap")
fgpar=folium.FeatureGroup(name="Paris")
fgusa=folium.FeatureGroup(name="USA")

def reading(data,col,lati,longi):

    if lati==48.8566:
        lat=list(data["lat"])
        lng=list(data["lng"])
        place=list(data["name"])
        for lt,ln,nm in zip(lat,lng, place):
            fgpar.add_child(folium.CircleMarker(location=[lt, ln], radius=12, popup=str(nm), fill_color=col, color='grey', fill=True, fill_opacity=0.9))
        map.add_child(fgpar)


    else:
        lat=list(data["LAT"])
        lng=list(data["LON"])
        elev=list(data["ELEV"])
        for lt,ln,el in zip(lat,lng, elev):
            fgusa.add_child(folium.Marker(location=[lt, ln], popup=str(el)+"m", icon=folium.Icon(color=color_producer(el))))
        map.add_child(fgusa)




reading(data1,"red",48.8566,2.3522)
reading(data2,"green",48.8566,2.3522)
reading(data3,"yellow",38.58,-99.09)

#representing population of all the countries using color based polygon features
fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000<= x['properties']['POP2005']< 20000000 else 'red'}))

map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
