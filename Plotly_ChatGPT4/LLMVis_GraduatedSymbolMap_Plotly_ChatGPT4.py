import pandas as pd
import plotly.express as px
import json

# Load the data from the CSV file
df = pd.read_csv('population2021.csv')

# Load the GeoJSON file
with open('countries.geojson') as f:
    geojson = json.load(f)

# Create the graduated symbol map
fig = px.scatter_geo(df, 
                     locations='ADMIN', # name of the dataframe column
                     size='Population', # name of the dataframe column
                     geojson=geojson, 
                     featureidkey="properties.ADMIN", # path to field in GeoJSON feature object with which to match the values passed in to locations
                     projection="natural earth"
                    )

# Show the plot
fig.show()
