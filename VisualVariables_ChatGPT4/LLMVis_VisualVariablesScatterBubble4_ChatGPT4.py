import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('iowa-electricityExtended.csv')

# Convert column 'A' to datetime
df['year'] = pd.to_datetime(df['year'])

# Normalize column 'D' to have values between 0 and 1 for opacity
df['consumption'] = (df['consumption'] - df['consumption'].min()) / (df['consumption'].max() - df['consumption'].min())

# Create a scatter plot with opacity encoding the values in column D
plt.scatter(df['year'], df['net_generation'], alpha=df['consumption'])

# Label the axes
plt.xlabel('year (time)')
plt.ylabel('net_generation (quantitative)')

# Display the chart
plt.show()
