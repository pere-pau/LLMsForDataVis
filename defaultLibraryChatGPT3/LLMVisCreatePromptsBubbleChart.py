import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
file_path = 'carsMod.csv'
df = pd.read_csv(file_path)

# Assuming 'A', 'B', and 'C' are the quantitative columns
# Replace 'A', 'B', and 'C' with your actual column names

# Create a bubble chart
plt.figure(figsize=(10, 6))
plt.scatter(df['mpg'], df['disp'], s=df['hp']*10, alpha=0.7, c='skyblue', edgecolors='black', linewidths=1)

# Set plot labels and title
plt.xlabel('Quantitative A')
plt.ylabel('Quantitative B')
plt.title('Bubble Chart')

# Show the plot
plt.show()
