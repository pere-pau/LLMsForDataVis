import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('iowa-electricityExtended.csv')

# Convert column 'A' to datetime
df['year'] = pd.to_datetime(df['year'])

# Define a dictionary of marker styles for each category in column 'B'
marker_dict = {'category1': 'o', 'category2': 's', 'category3': '^'}  # replace 'category1', 'category2', etc. with your actual categories

# Create a bubble chart with different shapes for each category
for category, marker in marker_dict.items():
    subset = df[df['source'] == category]
    plt.scatter(subset['year'], subset['net_generation'], s=subset['consumption'], marker=marker, label=category)

# Label the axes
plt.xlabel('year (time)')
plt.ylabel('net_generation (quantitative)')

# Add a legend
plt.legend()

# Display the chart
plt.show()
