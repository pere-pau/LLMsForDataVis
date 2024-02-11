# Import necessary libraries
import altair as alt
import pandas as pd

# Load the data from CSV file
data = pd.read_csv('mycarsUnique.csv')

# Create a grouped bar chart
chart = alt.Chart(data).mark_bar().encode(
    x=alt.X('Type:N', axis=alt.Axis(title='')),
    y='Price:Q',
    color='Type:N',
    column='Name:N'
)

# Display the chart
chart.show()
