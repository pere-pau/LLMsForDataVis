import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('myfile.csv')

# Group by column 'A' and sum column 'B'
grouped = df.groupby('A')['B'].sum()

# Create a pie chart
patches, texts, autotexts = plt.pie(grouped, labels=grouped.index, autopct='%1.1f%%')

# Make the labels bold
for text in texts:
    text.set_weight('bold')

# Display the chart
plt.show()
