import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('myfileDotPlot2Values.csv')

# Sort the dataframe by column 'A'
df = df.sort_values('A')

# Create a range plot using column 'B'
plt.hlines(y=df['A'], xmin=df.groupby('A')['B'].min(), xmax=df.groupby('A')['B'].max())

# Label the axes
plt.xlabel('B')
plt.ylabel('A')

# Display the chart
plt.show()
