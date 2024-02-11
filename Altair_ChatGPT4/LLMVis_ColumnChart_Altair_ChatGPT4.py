# Import necessary libraries
import altair as alt
import pandas as pd

# Load the data from CSV file
data = pd.read_csv('myfile.csv')

# Create a column chart
chart = alt.Chart(data).mark_bar().encode(
    x='A:N',
    y='B:Q'
)

# Display the chart
chart.show()
