import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('myfile.csv')

# Create a bar chart
plt.bar(df['A'], df['B'], color=['green' if b >= 0 else 'red' for b in df['B']])

# Label the axes
plt.xlabel('B')
plt.ylabel('A')

# Display the chart
plt.show()
