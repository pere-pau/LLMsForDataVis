# Import necessary libraries
import altair as alt
import pandas as pd
import json

# Load the data from CSV file
data = pd.read_csv('population2021.csv')

# Load the GeoJSON data
with open('countries.geojson') as file:
    geojson = json.load(file)

# Create a graduated symbol map
chart = alt.Chart(alt.Data(values=geojson['features'])).mark_circle().encode(
    longitude='properties.centroid[0]:Q',
    latitude='properties.centroid[1]:Q',
    size=alt.Size('Population:Q', legend=None),
    tooltip=['properties.ADMIN:N', alt.Tooltip('Population:Q', title='Population')]
).transform_lookup(
    lookup='properties.ADMIN',
    from_=alt.LookupData(data, 'ADMIN', ['Population'])
).project(
    type='identity', reflectY=True
).properties(
    width=500,
    height=300
)

# Display the chart
chart.show()
