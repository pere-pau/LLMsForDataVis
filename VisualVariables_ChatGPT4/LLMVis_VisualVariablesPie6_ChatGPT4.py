import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('myfile.csv')

# Group by column 'A' and sum 'B'
grouped = df.groupby('A')['B'].sum().sort_values(ascending=False)

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(grouped, labels=grouped.index, startangle=90, counterclock=False, autopct='%1.1f%%')

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

plt.show()
