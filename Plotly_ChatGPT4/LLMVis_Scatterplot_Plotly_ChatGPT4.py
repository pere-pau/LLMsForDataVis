import pandas as pd
import plotly.express as px

# Load the data from the CSV file
df = pd.read_csv('carsMod.csv')

# Create the scatter plot
fig = px.scatter(df, x='mpg', y='disp')

# Show the plot
fig.show()
