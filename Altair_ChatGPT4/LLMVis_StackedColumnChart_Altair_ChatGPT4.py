# Import necessary libraries
import altair as alt
import pandas as pd

# Load the data from CSV file
data = pd.read_csv('mycarsUnique.csv')

# Create a stacked column chart
chart = alt.Chart(data).mark_bar().encode(
    y='Name:N',
    x='Price:Q',
    color='Type:N'
)

# Display the chart
chart.show()
