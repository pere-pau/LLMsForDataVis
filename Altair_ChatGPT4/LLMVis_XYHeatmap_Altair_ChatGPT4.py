# Import necessary libraries
import altair as alt
import pandas as pd

# Load the data from CSV file
data = pd.read_csv('heatmapDataOrig.csv')

# Create an XY heatmap
chart = alt.Chart(data).mark_rect().encode(
    x='A:N',
    y='B:N',
    color='C:Q'
)

# Display the chart
chart.show()
