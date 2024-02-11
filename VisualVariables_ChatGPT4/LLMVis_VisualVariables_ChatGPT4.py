import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('carsMod.csv')

# Create a scatter plot
plt.scatter(df['mpg'], df['disp'])

# Label the axes
plt.xlabel('mpg')
plt.ylabel('disp')

# Display the chart
plt.show()
