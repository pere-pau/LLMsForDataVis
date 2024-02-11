import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('myfile.csv')

# Group by column 'A' and sum column 'B'
grouped = df.groupby('A')['B'].sum()

# Create a pie chart
plt.pie(grouped, labels = grouped.index, autopct='%1.1f%%')

# Display the chart
plt.show()
