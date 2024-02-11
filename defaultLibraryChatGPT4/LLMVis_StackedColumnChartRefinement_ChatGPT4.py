import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('mycars.csv')

# Group by columns 'Name' and 'Type' and sum column 'Price'
grouped = df.groupby(['Name', 'Type'])['Price'].sum().unstack()

# Create a stacked column chart
grouped.plot(kind='bar', stacked=True)

# Label the axes
plt.xlabel('Name')
plt.ylabel('Sum of Price')

# Display the chart
plt.show()
