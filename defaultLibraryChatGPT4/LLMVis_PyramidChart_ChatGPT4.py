import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('pyramiddata_Old.csv')

# Make the values in column 'Male' negative to create the left side of the pyramid
df['Male'] = df['Male'] * -1

# Create a bar chart for columns 'Male' and 'Female'
df.plot(kind='barh', x='Age Range', y=['Male', 'Female'], stacked=True, color=['blue', 'orange'])

# Label the axes
plt.xlabel('Quantity')
plt.ylabel('Age Range')

# Display the chart
plt.show()
