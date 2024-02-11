# Import necessary libraries
import altair as alt
import pandas as pd

# Load the data from CSV file
data = pd.read_csv('iowa-electricity.csv')

# Convert 'year' to datetime if it isn't already
data['year'] = pd.to_datetime(data['year'])

# Create an area chart
chart = alt.Chart(data).mark_area().encode(
    x='year:T',
    y='net_generation:Q',
    color='source:N'
)

# Display the chart
chart.show()
