import pandas as pd
import plotly.express as px

# Load the data from the CSV file
df = pd.read_csv('myfileDotPlot.csv')

# Create the violin plot
fig = px.violin(df, y='B', x='A', box=True, points="all")

# Show the plot
fig.show()
