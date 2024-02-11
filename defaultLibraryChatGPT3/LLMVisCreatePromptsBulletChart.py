import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data (replace 'myfile.csv' with your actual file path)
file_path = 'pyramiddata.csv'
df = pd.read_csv(file_path)

# Assuming 'A' is the categorical column, 'B' is the primary quantitative column,
# and 'C' is the secondary quantitative column
# Replace 'A', 'B', and 'C' with your actual column names

# Sort data by the primary value in descending order
df = df.sort_values(by='Male', ascending=False)

# Plot the bullet chart
fig, ax = plt.subplots(figsize=(10, 6))

# Set the positions for the categorical axis
positions = np.arange(len(df))

# Plot the primary values as bars
ax.barh(positions, df['Male'], color='skyblue', label='Primary Value')

# Plot the secondary values as points
ax.scatter(df['Female'], positions, color='orange', marker='o', s=100, label='Secondary Value')

# Set plot labels and title
ax.set_yticks(positions)
ax.set_yticklabels(df['Age Range'])
ax.set_xlabel('Value')
ax.set_title('Bullet Chart')

# Add a legend
ax.legend()

# Show the plot
plt.show()
