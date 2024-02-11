import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data from the CSV file
file_path = 'mycars.csv'
df = pd.read_csv(file_path)

# Assuming 'A' is the first categorical column, 'B' is the second categorical column,
# and 'C' is the quantitative column
# Replace 'A', 'B', and 'C' with your actual column names

# Create a pivot table for the stacked column chart
pivot_table = df.pivot_table(index='Name', columns='Type', values='Price', aggfunc='sum', fill_value=0)

# Set the bar width
bar_width = 0.8

# Create an array of categorical values
categories = np.arange(len(pivot_table.index))

# Create stacked column chart
fig, ax = plt.subplots(figsize=(10, 6))
bottoms = np.zeros(len(pivot_table.index))

for element in pivot_table.columns:
    ax.bar(categories, pivot_table[element], bar_width, label=element, bottom=bottoms)
    bottoms += np.array(pivot_table[element])

# Set plot labels and title
ax.set_xlabel('Category A')
ax.set_ylabel('Quantitative C')
ax.set_title('Stacked Column Chart')

# Set x-axis ticks and labels
ax.set_xticks(categories)
ax.set_xticklabels(pivot_table.index)

# Show the legend
ax.legend()

# Show the plot
plt.show()
