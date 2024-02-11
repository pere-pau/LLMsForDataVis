import pandas as pd
import plotly.express as px

# Load the data from the CSV file
df = pd.read_csv('myfileDotPlot.csv')

# Create the range plot
fig = px.line(df, x='A', y='B', range_y=[df['B'].min(), df['B'].max()])

# Show the plot
fig.show()
