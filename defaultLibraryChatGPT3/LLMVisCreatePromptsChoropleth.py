import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
file_path = 'population2021.csv'
df = pd.read_csv(file_path)

# Assuming 'A' is the column indicating the region and 'B' is the quantitative column
# Replace 'A' and 'B' with your actual column names

# Load the GeoJSON file containing region boundaries
geojson_path = 'countries.geojson'
gdf = gpd.read_file(geojson_path)

# Merge the GeoDataFrame with the CSV data
merged = gdf.merge(df, left_on='ADMIN', right_on='ADMIN', how='left')

# Create a choropleth map
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the GeoDataFrame with the choropleth color based on the quantitative column 'B'
merged.plot(column='Population', cmap='viridis', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Set plot labels and title
ax.set_title('Choropleth Map')
ax.set_axis_off()

# Show the plot
plt.show()
