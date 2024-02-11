# Import necessary libraries
import altair as alt
import pandas as pd

# Load the data from CSV file
data = pd.read_csv('myfileDotPlot.csv')

# Create a box plot
chart = alt.Chart(data).mark_boxplot().encode(
    x='A:N',
    y='B:Q'
)

# Display the chart
chart.show()
