import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
file_path = 'myfile.csv'
df = pd.read_csv(file_path)

# Assuming 'A' is the categorical column and 'B' is the quantitative column
# Replace 'A' and 'B' with your actual column names

# Create a simple pictogram chart
fig, ax = plt.subplots(figsize=(10, 6))

# Scatter plot with custom marker size based on the quantitative column 'B'
ax.scatter(df.index, [1] * len(df), s=df['B'] * 10, alpha=0.7)

# Set plot labels and title
ax.set_xlabel('Category A')
ax.set_ylabel('Pictograms')
ax.set_title('Pictogram Chart')

# Remove y-axis ticks and labels
ax.set_yticks([])
ax.set_yticklabels([])

# Show the plot
plt.show()
