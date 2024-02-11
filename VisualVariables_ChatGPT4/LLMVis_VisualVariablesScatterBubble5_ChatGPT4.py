import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('iowa-electricityExtended.csv')

# Convert column 'A' to datetime and then to numeric for sizing
df['year'] = pd.to_datetime(df['year'])
df['year'] = df['year'].apply(lambda x: x.timestamp())

# Create a scatter plot with size defined by column 'A'
plt.scatter(df['net_generation'], df['consumption'], s=df['year'])

# Label the axes
plt.xlabel('net_generation (quantitative)')
plt.ylabel('consumption (quantitative)')

# Display the chart
plt.show()
