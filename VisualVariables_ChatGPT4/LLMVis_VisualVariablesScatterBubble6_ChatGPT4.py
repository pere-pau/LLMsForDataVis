import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('iowa-electricityExtended.csv')

# Convert column 'A' to datetime
df['year'] = pd.to_datetime(df['year'])

# Define a dictionary of marker styles for each category in column 'B'
marker_dict = {'category1': 'o', 'category2': 's', 'category3': '^'}  # replace 'category1', 'category2', etc. with your actual categories

# Normalize column 'D' to have values between 0 and 20 for sizing
df['consumption'] = (df['consumption'] - df['consumption'].min()) / (df['consumption'].max() - df['consumption'].min()) * 20

# Create a scatter plot with different shapes for each category and sizes dependent on column D
for category, marker in marker_dict.items():
    subset = df[df['source'] == category]
    plt.scatter(subset['net_generation'], subset['consumption'], s=subset['consumption'], marker=marker, label=category)

# Label the axes
plt.xlabel('net_generation (quantitative)')
plt.ylabel('consumption (quantitative)')

# Add a legend
plt.legend()

# Display the chart
plt.show()
