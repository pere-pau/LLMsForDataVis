import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data from the CSV file
file_path = 'mycarsUnique.csv'
df = pd.read_csv(file_path)

# Assuming 'A' is the first categorical column, 'B' is the second categorical column,
# and 'C' is the quantitative column
# Replace 'A', 'B', and 'C' with your actual column names

# Create a pivot table for the grouped bar chart
pivot_table = df.pivot_table(index='Name', columns='Type', values='Price', aggfunc='sum', fill_value=0)

# Set the bar width
bar_width = 0.35

# Create an array of categorical values
categories = np.arange(len(pivot_table.index))

# Create grouped bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bar1 = ax.bar(categories - bar_width/2, pivot_table.iloc[:, 0], bar_width, label=pivot_table.columns[0])
bar2 = ax.bar(categories + bar_width/2, pivot_table.iloc[:, 1], bar_width, label=pivot_table.columns[1])

# Set plot labels and title
ax.set_xlabel('Category Name')
ax.set_ylabel('Quantitative Price')
ax.set_title('Grouped Bar Chart')

# Set x-axis ticks and labels
ax.set_xticks(categories)
ax.set_xticklabels(pivot_table.index)

# Show the legend
ax.legend()

# Show the plot
plt.show()
