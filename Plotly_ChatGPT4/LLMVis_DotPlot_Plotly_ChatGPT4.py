import pandas as pd
import plotly.express as px

# Load the data from the CSV file
df = pd.read_csv('myfileDotPlot.csv')

# Create the dot plot
fig = px.scatter(df, x='B', y='A', orientation='h')

# Show the plot
fig.show()
