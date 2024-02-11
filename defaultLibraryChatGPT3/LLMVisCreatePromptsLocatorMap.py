import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
file_path = 'airports.csv'
df = pd.read_csv(file_path)

# Assuming 'name' is the column for the name of the object, 'latitude' and 'longitude' are the columns for coordinates
# Replace 'name', 'latitude', and 'longitude' with your actual column names

# Create a GeoDataFrame from the CSV data
gdf_points = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['longitude'], df['latitude']))

# Load the GeoJSON file containing region boundaries
geojson_path = 'us-states.json'
gdf_regions = gpd.read_file(geojson_path)

# Create a locator map
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the GeoDataFrame with points for the objects
gdf_points.plot(ax=ax, color='red', marker='o', markersize=50, alpha=0.7)

# Plot the GeoDataFrame with region boundaries
gdf_regions.plot(ax=ax, color='none', edgecolor='black', linewidth=1)

# Set plot labels and title
ax.set_title('Locator Map')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# Show the plot
plt.show()
