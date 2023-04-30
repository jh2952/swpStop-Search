import pandas as pd
import folium
from folium.plugins import MarkerCluster

i = 0

# Map defined with coordinates centred on Wales. 
my_map = folium.Map(location = [52.1307, -3.7837], zoom_start = 8, tiles="Stamen Toner" ) 

# This Loop will go through all files and pull out location
# data and plot it out on the map defined above.

while i < 36:
    
    j = 0
    
    mCluster = MarkerCluster(name = "Stop and Search Data, Month {}".format(i)).add_to(my_map)
    
    df = pd.read_csv("C:/Users/Jack/Desktop/S&S Map/Concatenation/{}.csv".format(i))
    df = df.dropna(subset = ['Longitude'])
    df = df.dropna(subset = ['Latitude'])
    df.columns = [c.replace(' ', '_') for c in df.columns]
    df.columns = [c.replace('-', '_') for c in df.columns]
    
    print("File {} Complete.".format(i))
    
    dat = df.Date.tolist()
    lat = df.Latitude.tolist()
    lon = df.Longitude.tolist()
    gen =  df.Gender.tolist()
    age = df.Age_range.tolist()
    eth = df.Officer_defined_ethnicity.tolist()
    leg = df.Legislation.tolist()
    out = df.Outcome.tolist()
    
    # This loop plots the individual stop and searches onto the map, pulled
    # from the concatenated file sorted above.
    
    while j < len(lat):
        string = "Date: *{}*, Lat: *{}*, Lon: *{}*, Gender: *{}*, Age: *{}*, Ethnicity: *{}*, Legislation: *{}*, Outcome: *{}*".format(dat[j] ,lat[j], lon[j], gen[j], age[j], eth[j], leg[j], out[j])
        folium.Marker([lat[j], lon[j]], popup = string).add_to(mCluster)
        j = j + 1
    
    i = i + 1
    
print("Saving Map...")

my_map.add_child(folium.LayerControl())
my_map.save("final.html")

print("Map Saved!")
        
    