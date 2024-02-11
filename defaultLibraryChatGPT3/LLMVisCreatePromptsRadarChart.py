import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data from the CSV file
file_path = 'iowa-electricityShort.csv'
df = pd.read_csv(file_path)

# Assuming 'A' is the categorical column, 'B' is the second categorical column,
# and 'C' is the quantitative column
# Replace 'A', 'B', and 'C' with your actual column names

# Pivot the data to make it suitable for a radar chart
pivot_table = df.pivot_table(index='year', columns='source', values='net_generation', aggfunc='mean', fill_value=0)

# Number of variables
num_vars = len(pivot_table.columns)

# Compute angle of each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Repeat the first value to close the circular plot
values = pivot_table.iloc[0].tolist()
values += values[:1]

# Plot the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='blue', alpha=0.25)

# Plot each individual's data
for i, row in pivot_table.iterrows():
    values = row.tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=i)

# Add labels and legend
ax.set_thetagrids(np.degrees(angles), pivot_table.columns)
ax.set_title('Radar Chart')

# Add a legend
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Show the plot
plt.show()
