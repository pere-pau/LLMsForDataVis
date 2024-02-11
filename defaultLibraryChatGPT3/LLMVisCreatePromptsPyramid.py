import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
file_path = 'pyramiddata.csv'
df = pd.read_csv(file_path)

# Assuming 'A' is the categorical column (age ranges), 'B' and 'C' are quantitative columns
# Replace 'A', 'B', and 'C' with your actual column names

# Sort the DataFrame by the categorical column
df = df.sort_values(by='Age Range')

# Create a pyramid chart
fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars on the left side of the y-axis
ax.barh(df['Age Range'], df['Male'], color='blue', label='Category B')

# Plot bars on the right side of the y-axis (multiply by -1 to reverse direction)
ax.barh(df['Age Range'], -df['Female'], color='orange', label='Category C')

# Set plot labels and title
ax.set_xlabel('Quantitative Values')
ax.set_ylabel('Age Ranges')
ax.set_title('Pyramid Chart')

# Adjust x-axis ticks
max_value = max(df['Male'].max(), df['Female'].max())
ax.set_xticks([-max_value, 0, max_value])
ax.set_xticklabels([f"{abs(max_value)}", "0", f"{max_value}"])

# Show the legend
ax.legend()

# Show the plot
plt.show()
