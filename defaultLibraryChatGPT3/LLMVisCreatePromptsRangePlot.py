import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from the CSV file
file_path = 'myfileDotPlot.csv'
df = pd.read_csv(file_path)

# Assuming 'A' is the categorical column and 'B' is the quantitative column
# Replace 'A' and 'B' with your actual column names

# Create a range plot using seaborn
sns.lineplot(x='A', y='B', data=df, ci='sd')

# Set plot labels and title
plt.xlabel('Category A')
plt.ylabel('Quantitative B')
plt.title('Range Plot')

# Show the plot
plt.show()
