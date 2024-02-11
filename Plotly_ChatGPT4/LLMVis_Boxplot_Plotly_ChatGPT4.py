import pandas as pd
import plotly.express as px

# Load the data from the CSV file
df = pd.read_csv('myfileDotPlot.csv')

# Create the box plot
fig = px.box(df, x='A', y='B')

# Show the plot
fig.show()
