import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('carsMod.csv')

# Create a scatter plot with column 'C' determining the size of the bubbles
plt.scatter(df['mpg'], df['disp'], s=df['hp'])

# Label the axes
plt.xlabel('npg')
plt.ylabel('disp')

# Display the chart
plt.show()
