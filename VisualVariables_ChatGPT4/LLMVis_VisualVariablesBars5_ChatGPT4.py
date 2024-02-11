import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the CSV file
df = pd.read_csv('myfile.csv')

# Create a color array
colors = plt.cm.viridis(np.linspace(0, 1, len(df)))

# Create a bar chart with different colors
plt.bar(df['A'], df['B'], color=colors)

# Label the axes
plt.xlabel('B')
plt.ylabel('A')

# Display the chart
plt.show()
