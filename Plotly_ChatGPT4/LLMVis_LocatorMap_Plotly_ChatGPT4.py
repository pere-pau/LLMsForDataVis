import pandas as pd
import plotly.express as px
import json

# Load the data from the CSV file
df = pd.read_csv('airports.csv')

# Load the GeoJSON file
with open('us-states.json') as f:
    geojson = json.load(f)

# Create the locator map
fig = px.scatter_geo(df, 
                     lat='latitude', 
                     lon='longitude', 
                     hover_name='name', 
                     projection="natural earth"
                    )

# Show the plot
fig.show()
