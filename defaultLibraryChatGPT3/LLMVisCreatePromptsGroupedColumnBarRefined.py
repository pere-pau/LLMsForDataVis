import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data from the CSV file
file_path = 'mycarsUnique.csv'
df = pd.read_csv(file_path)

# Assuming 'A' is the first categorical column, 'B' is the second categorical column,
# and 'C' is the quantitative column
# Replace 'A', 'B', and 'C' with your actual column names

# Get unique elements from column 'B'
unique_elements_B = df['Type'].unique()

# Create a pivot table for the grouped bar chart
pivot_table = df.pivot_table(index='Name', columns='Type', values='Price', aggfunc='sum', fill_value=0)

# Set the bar width
bar_width = 0.2  # Adjust as needed

# Create an array of categorical values
categories = np.arange(len(pivot_table.index))

# Create grouped bar chart with dynamic number of columns
fig, ax = plt.subplots(figsize=(12, 6))

for i, element in enumerate(unique_elements_B):
    bar_position = categories + i * bar_width - (len(unique_elements_B) - 1) * bar_width / 2
    bars = ax.bar(bar_position, pivot_table[element], bar_width, label=element)

# Set plot labels and title
ax.set_xlabel('Category A')
ax.set_ylabel('Quantitative C')
ax.set_title('Grouped Bar Chart')

# Set x-axis ticks and labels
ax.set_xticks(categories)
ax.set_xticklabels(pivot_table.index)

# Show the legend
ax.legend()

# Show the plot
plt.show()
