# Import necessary libraries
import altair as alt
import pandas as pd

# Load the data from CSV file
data = pd.read_csv('myfileDotPlot.csv')

# Create a dot plot
chart = alt.Chart(data).mark_circle(size=60).encode(
    x='B:Q',
    y='A:N'
)

# Display the chart
chart.show()
