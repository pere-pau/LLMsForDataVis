import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
file_path = 'mycars.csv'
df = pd.read_csv(file_path)

# Assuming 'A' is the first categorical column, 'B' is the second categorical column, 
# and 'C' is the quantitative column
# Replace 'A', 'B', and 'C' with your actual column names

# Create a pivot table for the stacked bar chart
pivot_table = df.pivot_table(index='Name', columns='Type', values='Price', aggfunc='sum', fill_value=0)

# Create a stacked bar chart
pivot_table.plot(kind='bar', stacked=True, figsize=(10, 6))

# Set plot labels and title
plt.xlabel('Category A')
plt.ylabel('Quantitative C')
plt.title('Stacked Bar Chart')

# Show the legend
plt.legend(title='Category B', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.show()
