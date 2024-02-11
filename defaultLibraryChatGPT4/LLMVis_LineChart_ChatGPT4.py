import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('iowa-electricity.csv')

# Convert column 'A' to datetime
df['year'] = pd.to_datetime(df['year'])

# Pivot the dataframe to have categories from column 'B' as columns
df_pivot = df.pivot(index='year', columns='source', values='net_generation')

# Create a line chart
df_pivot.plot()

# Label the axes
plt.xlabel('Time')
plt.ylabel('Quantity')

# Display the chart
plt.show()