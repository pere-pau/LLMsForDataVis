import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the CSV file
df = pd.read_csv('iowa-electricityShort.csv')

# Pivot the dataframe to have categories from column 'source' as columns 
## NOTE: SWAPPED THE INDEX AND COLUMNS VALUES TO MAKE IT WORK
print('## NOTE: SWAPPED THE INDEX AND COLUMNS VALUES TO MAKE IT WORK')
df_pivot = df.pivot(index='source', columns='year', values='net_generation')

# Number of variables we're plotting.
num_vars = len(df_pivot.columns)

# Split the circle into even parts and save the angles
# so we know where to put each axis.
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is a circle, so we need to "complete the loop"
# and append the start value to the end.
angles += angles[:1]

# ax = plt.subplot(polar=True)
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Helper function to plot each row of the DataFrame.
def add_to_plot(row):
    values = row.values.flatten().tolist()
    values += values[:1] # repeat the first value to close the circular graph
    ax.fill(angles, values, color='red', alpha=0.25)

# Apply the helper function to each row.
df_pivot.apply(add_to_plot, axis=1)

# Set the y-labels all around the circumference.
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(df_pivot.columns)

plt.show()
