# Import necessary libraries
import altair as alt
import pandas as pd
import json

# Load the data from CSV file
data = pd.read_csv('airports.csv')

# Load the GeoJSON data
with open('us-states.json') as file:
    geojson = json.load(file)

# Create a base map
base = alt.Chart(alt.Data(values=geojson['features'])).mark_geoshape(
    fill='lightgray',
    stroke='white'
).project('identity')

# Create a point layer for the objects
points = alt.Chart(data).mark_circle().encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    tooltip=['name:N', 'latitude:Q', 'longitude:Q']
)

# Combine the base map and point layer
chart = alt.layer(base, points).properties(
    width=500,
    height=300
)

# Display the chart
chart.show()
