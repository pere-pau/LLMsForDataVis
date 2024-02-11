import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from the CSV file
file_path = 'iowa-electricity.csv'
df = pd.read_csv(file_path)

# Assuming 'A' is the time column, 'B' is the categorical column, and 'C' is the quantitative column
# Replace 'A', 'B', and 'C' with your actual column names

# Create a DataFrame pivot table for the area chart
pivot_table = df.pivot_table(index='year', columns='source', values='net_generation', aggfunc='sum', fill_value=0)

# Create an area chart using seaborn
sns.set(style="whitegrid")
pivot_table.plot(kind='area', stacked=True, alpha=0.7)

# Set plot labels and title
plt.xlabel('Time (year)')
plt.ylabel('Quantitative net_generation')
plt.title('Area Chart')

# Show the plot
plt.show()
