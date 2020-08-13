import folium
import pandas
data = pandas.read_csv('Volcanoes.txt', sep=',')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
m = folium.Map(location=[lat[0], lon[0]], zoom_start=6)


def colour(el):
    if 0 < el < 1000:
        return 'lightgreen'
    elif 1000 < el < 2000:
        return 'green'
    elif 2000 < el < 3000:
        return 'orange'
    elif el > 3000:
        return 'red'


# Adding Objects to the map using feature group
fgv = folium.FeatureGroup(name='Volcanos')

# Can get blank page if child text string has ''' in it,
# do this = (str(str), parse_html=True)
# Multiple marker

for i, j, e in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker
                 (location=tuple([i, j]),
                  radius=10,
                  popup='{} m'.format(str(e)),
                  fill_color=colour(e),
                  color='grey',
                  fill=True,
                  fill_opacity=0.7))

# adding polygons.
fgl = folium.FeatureGroup(name='Population')
fgl.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(),

    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Adding feature gri=oup to main folium objets
m.add_child(fgv)
m.add_child(fgl)

# Layer COntrol
m.add_child(folium.LayerControl())


m.save('map2.html')
