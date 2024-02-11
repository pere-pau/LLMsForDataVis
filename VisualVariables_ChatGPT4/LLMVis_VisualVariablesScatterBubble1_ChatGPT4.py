import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

# Load the data from the CSV file
df = pd.read_csv('iowa-electricityExtended.csv')

# Convert column 'A' to datetime
df['year'] = pd.to_datetime(df['year'])

# Create a new figure
fig, ax = plt.subplots()

# Create a collection of triangle patches for the scatter plot
patches = []
for i in range(len(df)):
    triangle = mpatches.RegularPolygon((df.iloc[i]['year'], df.iloc[i]['net_generation']), numVertices=3, radius=5, orientation=df.iloc[i]['consumption'])
    patches.append(triangle)

collection = PatchCollection(patches)

# Add the collection to the axes
ax.add_collection(collection)

# Set the limits of the axes
ax.set_xlim(df['year'].min(), df['year'].max())
ax.set_ylim(df['net_generation'].min(), df['net_generation'].max())

# Label the axes
plt.xlabel('year (time)')
plt.ylabel('net_generation (quantitative)')

# Display the chart
plt.show()
