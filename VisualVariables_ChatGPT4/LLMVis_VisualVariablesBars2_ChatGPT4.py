import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('myfile.csv')

# Create a bar chart with light green bars
plt.bar(df['A'], df['B'], color='lightgreen')

# Label the axes
plt.xlabel('B')
plt.ylabel('A')

# Display the chart
plt.show()
