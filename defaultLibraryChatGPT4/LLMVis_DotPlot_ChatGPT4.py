import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('myfileDotPlot.csv')

# Create a dot plot using columns 'A' and 'B'
plt.scatter(df['B'], df['A'])

# Label the axes
plt.xlabel('B')
plt.ylabel('A')

# Display the chart
plt.show()
