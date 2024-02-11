import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('heatmapDataOrig.csv')

# Pivot the dataframe to create a matrix for the heatmap
df_pivot = df.pivot(index='A', columns='B', values='C')

# Create a heatmap
sns.heatmap(df_pivot)

# Display the chart
plt.show()
