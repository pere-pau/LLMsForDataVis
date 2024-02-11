import pandas as pd
import plotly.express as px
import json


# Load the data from the CSV file
df = pd.read_csv('population2021.csv')

# Load the GeoJSON file
with open('countries.geojson') as f:
    geojson = json.load(f)

# Create the Choropleth chart
fig = px.choropleth(df, geojson=geojson, 
                    locations='ADMIN', # name of the dataframe column
                    color='Population', # name of the dataframe column
                    featureidkey="properties.ADMIN", # path to field in GeoJSON feature object with which to match the values passed in to locations
                    projection="mercator"
                   )

# Show the plot
fig.update_geos(showcountries=False, showcoastlines=True, showland=True, fitbounds="locations")

fig.show()



