import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('myfile.csv')

# Create a horizontal bar chart
plt.barh(df['A'], df['B'])

# Label the axes
plt.xlabel('B')
plt.ylabel('A')

# Display the chart
plt.show()
