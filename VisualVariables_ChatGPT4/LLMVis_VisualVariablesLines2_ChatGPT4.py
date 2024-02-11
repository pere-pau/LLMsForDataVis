import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('iowa-electricity.csv')

# Convert column 'A' to datetime
df['year'] = pd.to_datetime(df['year'])

# Pivot the dataframe to have 'B' values as columns, 'A' as index and 'C' as values
df_pivot = df.pivot(index='year', columns='source', values='net_generation')

# Create a line chart with linewidth of 2 (approximately 20 pixels for a typical display)
for column in df_pivot.columns:
    plt.plot(df_pivot.index, df_pivot[column], linewidth=2)

# Label the axes
plt.xlabel('year (time)')
plt.ylabel('net_generation (quantitative)')

# Display the chart
plt.show()
