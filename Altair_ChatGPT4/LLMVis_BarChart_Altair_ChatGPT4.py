# Import necessary libraries
import altair as alt
import pandas as pd

# Load the data from CSV file
data = pd.read_csv('myfile.csv')

# Create a bar chart
chart = alt.Chart(data).mark_bar().encode(
    x='A',
    y='B'
)

# Display the chart
chart.show()
