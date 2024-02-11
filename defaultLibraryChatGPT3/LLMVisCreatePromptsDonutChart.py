import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
file_path = 'myfile.csv'
df = pd.read_csv(file_path)

# Assuming 'A' is the categorical column and 'B' is the quantitative column
# Replace 'A' and 'B' with your actual column names

# Group by the categorical column and calculate the sum of the quantitative column
grouped_data = df.groupby('A')['B'].sum().reset_index()

# Create a donut chart
plt.figure(figsize=(8, 8))  # Adjust figure size if needed

# Outer pie chart
outer_colors = plt.cm.tab20c.colors
outer_pie = plt.pie(grouped_data['B'], labels=grouped_data['A'], autopct='%1.1f%%', startangle=90,
                       pctdistance=0.85, colors=outer_colors)

# Inner pie chart (white color to create the 'hole' in the donut)
inner_pie = plt.pie([1], radius=0.75, colors=['w'])

# Set aspect ratio to be equal so that the donut is circular
plt.axis('equal')

# Set plot title
plt.title('Donut Chart')

# Show the plot
plt.show()
