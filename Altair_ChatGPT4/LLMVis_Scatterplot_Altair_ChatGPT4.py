# Import necessary libraries
import altair as alt
import pandas as pd

# Load the data from CSV file
data = pd.read_csv('carsMod.csv')

# Create a scatter plot
chart = alt.Chart(data).mark_circle().encode(
    x='mpg:Q',
    y='disp:Q'
)

# Display the chart
chart.show()
