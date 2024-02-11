import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from the CSV file
file_path = 'iowa-electricity.csv'
df = pd.read_csv(file_path)

# Assuming 'A' is the time column, 'B' is the categorical column, and 'C' is the quantitative column
# Replace 'A', 'B', and 'C' with your actual column names

# Create a line chart using seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))  # Adjust figure size if needed
sns.lineplot(x='year', y='net_generation', hue='source', data=df, marker='o')

# Set plot labels and title
plt.xlabel('Time (A)')
plt.ylabel('Quantitative C')
plt.title('Line Chart')

# Show the legend
plt.legend(title='Category B', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.show()
