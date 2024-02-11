import pandas as pd
import plotly.express as px

# Load the data from the CSV file
df = pd.read_csv('iowa-electricityPolar.csv')

# Create the radar chart
fig = px.line_polar(df, r='net_generation', theta='year', color='source', line_close=True)

# Show the plot
fig.show()
