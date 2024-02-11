import pandas as pd
import plotly.express as px

# Load the data from the CSV file
df = pd.read_csv('iowa-electricity.csv')

# Convert the 'year' column to datetime
df['year'] = pd.to_datetime(df['year'])

# Create the line chart
fig = px.line(df, x='year', y='net_generation', color='source')

# Show the plot
fig.show()




