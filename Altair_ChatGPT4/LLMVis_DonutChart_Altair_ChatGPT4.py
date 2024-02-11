# Import necessary libraries
import altair as alt
import pandas as pd

# Load the data from CSV file
data = pd.read_csv('myfile.csv')

# Create a pie chart
chart = alt.Chart(data).transform_window(
    index='count()'
).transform_fold(
    ['B']
).mark_arc(
    cornerRadius=5,
    innerRadius=50  # This line makes the chart a donut chart
).encode(
    theta='B:Q',
    color='A:N',
    detail='index:N',
    tooltip=['A', 'B']
).properties(
    width=400,
    height=400
)

# Display the chart
chart.show()
