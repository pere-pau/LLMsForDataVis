import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
file_path = 'myfile.csv'
df = pd.read_csv(file_path)

# Assuming 'A' is the categorical column and 'B' is the quantitative column
# Replace 'A' and 'B' with your actual column names

# Group by the categorical column and calculate the mean of the quantitative column
grouped_data = df.groupby('A')['B'].mean().reset_index()

# Create a bar chart
plt.bar(grouped_data['A'], grouped_data['B'])

# Set plot labels and title
plt.xlabel('Category A')
plt.ylabel('Mean of Quantitative B')
plt.title('Bar Chart')

# Show the plot
plt.show()
