
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('airports.csv')

# Convert the DataFrame to a GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))

# Load the GeoJSON file
regions = gpd.read_file('us-states.json')

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the regions
regions.plot(ax=ax)

# Plot the points from the GeoDataFrame
gdf.plot(ax=ax, color='red')

# Display the map
plt.show()
