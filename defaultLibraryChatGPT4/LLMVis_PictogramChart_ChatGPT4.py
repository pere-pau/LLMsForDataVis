import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('myfile.csv')

# Create a figure and axes
fig, ax = plt.subplots()

# Create a scatter plot with custom markers
for i, category in enumerate(df['A'].unique()):
    df_category = df[df['A'] == category]
    ax.scatter(df_category['A'], df_category['B'], marker=f'${i}$', s=100)

# Display the chart
plt.show()
