import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('population2021.csv')

# Load the GeoJSON file
gdf = gpd.read_file('countries.geojson')

# Merge the dataframes on the 'A' column
merged = gdf.set_index('ADMIN').join(df.set_index('ADMIN'))

# Create a choropleth
fig, ax = plt.subplots(1, 1)
merged.plot(column='Population', ax=ax, legend=True)

# Display the chart
plt.show()

