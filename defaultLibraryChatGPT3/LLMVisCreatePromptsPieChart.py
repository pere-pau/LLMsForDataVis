import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
file_path = 'myfile.csv'
df = pd.read_csv(file_path)

# Assuming 'A' is the categorical column and 'B' is the quantitative column
# Replace 'A' and 'B' with your actual column names

# Group by the categorical column and calculate the sum of the quantitative column
grouped_data = df.groupby('A')['B'].sum().reset_index()

# Create a pie chart
plt.figure(figsize=(8, 8))  # Adjust figure size if needed
plt.pie(grouped_data['B'], labels=grouped_data['A'], autopct='%1.1f%%', startangle=140)

# Set plot title
plt.title('Pie Chart')

# Show the plot
plt.show()
