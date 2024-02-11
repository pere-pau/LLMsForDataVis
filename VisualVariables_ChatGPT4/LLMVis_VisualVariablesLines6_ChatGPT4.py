import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('iowa-electricity.csv')

# Convert column 'A' to datetime
df['year'] = pd.to_datetime(df['year'])

# Pivot the data so each category in 'B' has its own column
pivot_df = df.pivot(index='year', columns='source', values='net_generation')

# Create the line chart with stroked lines
fig, ax = plt.subplots()
pivot_df.plot(kind='line', style='--', ax=ax)

plt.show()
