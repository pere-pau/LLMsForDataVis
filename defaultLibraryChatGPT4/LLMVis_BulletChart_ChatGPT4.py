import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('pyramiddata.csv')

# Create a figure and a set of subplots
fig, axs = plt.subplots(len(df['Age Range']), 1, figsize=(5, len(df['Age Range'])*2))

# Generate a bullet chart for each row in the dataframe
for idx, ax in enumerate(axs):
    ax.set_aspect('auto')
    ax.broken_barh([(0, df['Male'][idx])], (0.1, 0.9), facecolors='blue')
    ax.broken_barh([(0, df['Female'][idx])], (0.1, 0.9), facecolors='red')
    ax.set_yticks([0.5])
    ax.set_yticklabels([df['Age Range'][idx]])
    ax.set_xlim(0, max(df['Male'].max(), df['Female'].max())*1.1)

plt.tight_layout()
plt.show()
