import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('myfile.csv')

# Group by column 'A' and sum column 'B'
grouped = df.groupby('A')['B'].sum()

# Create a pie chart
plt.pie(grouped, labels = grouped.index, autopct='%1.1f%%', wedgeprops=dict(width=0.3))

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Display the chart
plt.show()
