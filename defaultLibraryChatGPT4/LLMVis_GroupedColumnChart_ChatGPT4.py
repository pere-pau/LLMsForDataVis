import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('mycarsUnique.csv')

# Pivot the dataframe to have categories from column 'B' as columns
df_pivot = df.pivot(index='Name', columns='Type', values='Price')

# Create a grouped column chart
df_pivot.plot(kind='bar')

# Label the axes
plt.xlabel('Name')
plt.ylabel('Price')

# Display the chart
plt.show()
