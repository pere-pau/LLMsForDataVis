import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('myfile.csv')

# Create a bar chart using columns 'A' and 'B'
plt.bar(df['A'], df['B'])

# Label the axes
plt.xlabel('A')
plt.ylabel('B')

# Display the chart
plt.show()
