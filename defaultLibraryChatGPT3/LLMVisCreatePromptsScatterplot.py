import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
file_path = 'carsMod.csv'
df = pd.read_csv(file_path)

# Assuming 'A' and 'B' are the quantitative columns
# Replace 'A' and 'B' with your actual column names

# Create a scatterplot
plt.figure(figsize=(10, 6))
plt.scatter(df['mpg'], df['disp'], s=50, alpha=0.7)

# Set plot labels and title
plt.xlabel('Quantitative A')
plt.ylabel('Quantitative B')
plt.title('Scatterplot')

# Show the plot
plt.show()
