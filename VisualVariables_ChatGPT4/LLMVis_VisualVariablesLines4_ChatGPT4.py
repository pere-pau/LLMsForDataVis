import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('iowa-electricity.csv')

# Convert column 'A' to datetime
df['year'] = pd.to_datetime(df['year'])

# Pivot the dataframe to have 'B' values as columns, 'A' as index and 'C' as values
df_pivot = df.pivot(index='year', columns='source', values='net_generation')

# Create a line chart marking the data points with circles
for column in df_pivot.columns:
    plt.plot(df_pivot.index, df_pivot[column], marker='o')

# Label the axes
plt.xlabel('year (time)')
plt.ylabel('net_generation (quantitative)')

# Display the chart
plt.show()
