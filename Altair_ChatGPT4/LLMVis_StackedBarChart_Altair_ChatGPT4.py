# Import necessary libraries
import altair as alt
import pandas as pd

# Load the data from CSV file
data = pd.read_csv('mycarsUnique.csv')

# Create a stacked bar chart
chart = alt.Chart(data).mark_bar().encode(
    x='Name:N',
    y='Price:Q',
    color='Type:N'
)

# Display the chart
chart.show()
