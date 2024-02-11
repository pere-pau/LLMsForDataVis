import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('myfile.csv')

# Create a bar chart
bars = plt.bar(df['A'], df['B'])

# Label the axes
plt.xlabel('B')
plt.ylabel('A')

# Add labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), va='bottom')  # va: vertical alignment

# Display the chart
plt.show()
