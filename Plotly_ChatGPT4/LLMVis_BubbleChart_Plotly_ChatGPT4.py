import pandas as pd
import plotly.express as px

# Load the data from the CSV file
df = pd.read_csv('carsMod.csv')

# Create the bubble chart
fig = px.scatter(df, x='mpg', y='disp', size='hp')

# Show the plot
fig.show()
