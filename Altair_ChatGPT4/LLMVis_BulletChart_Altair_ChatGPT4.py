# Import necessary libraries
import altair as alt
import pandas as pd

# Load the data from CSV file
data = pd.read_csv('pyramiddata.csv')

# Define base chart
base = alt.Chart(data).encode(
    alt.X('Male:Q', title='Value'),
    alt.Y('Age Range:N', title='Category')
)

# Define bar chart for 'B' values
bar = base.mark_bar(color='skyblue').encode(
    alt.X('Male:Q', title='Value')
)

# Define line chart for 'C' values
line = base.mark_tick(color='black', thickness=2, size=30).encode(
    alt.X('Female:Q', title='Second Value')
)

# Combine bar and line chart
chart = alt.layer(bar, line)

# Display the chart
chart.show()
