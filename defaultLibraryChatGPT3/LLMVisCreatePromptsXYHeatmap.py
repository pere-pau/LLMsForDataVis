import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from the CSV file
file_path = 'heatmapData.csv'
df = pd.read_csv(file_path)

# Assuming 'A' is the first categorical column, 'B' is the second categorical column,
# and 'C' is the quantitative column
# Replace 'A', 'B', and 'C' with your actual column names

# Pivot the data to create a matrix suitable for a heatmap
heatmap_data = df.pivot_table(index='A', columns='B', values='C', aggfunc='mean', fill_value=0)

# Create an XY heatmap using seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, cmap='viridis', annot=True, fmt=".2f", linewidths=.5)

# Set plot labels and title
plt.xlabel('Category B')
plt.ylabel('Category A')
plt.title('XY Heatmap Chart')

# Show the plot
plt.show()
