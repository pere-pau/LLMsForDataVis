import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('myfilePosNeg.csv')

# Calculate the figure width needed for bars of approximately 120 pixels wide
bar_width_in_inches = 120 / plt.gcf().dpi
num_bars = df['A'].nunique()
fig_width = num_bars * bar_width_in_inches

# Create a new figure with the calculated width and a fixed height
fig, ax = plt.subplots(figsize=(fig_width, 6))

# Create a bar chart
ax.bar(df['A'], df['B'])

# Label the axes
ax.set_xlabel('B')
ax.set_ylabel('A')

# Display the chart
plt.show()
