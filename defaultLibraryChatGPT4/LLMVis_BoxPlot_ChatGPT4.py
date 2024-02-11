import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('myfileDotPlot.csv')

# Create a box plot
sns.boxplot(x='A', y='B', data=df)

# Display the chart
plt.show()
