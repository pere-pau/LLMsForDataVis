# Import necessary libraries
import altair as alt
import pandas as pd

# Load the data from CSV file
data = pd.read_csv('pyramiddata_Old.csv')

# Ensure 'Age Range' is sorted in the desired order
data['Age Range'] = pd.Categorical(data['Age Range'], categories=data['Age Range'].unique(), ordered=True)

# Create a pyramid chart
chart1 = alt.Chart(data).mark_bar().encode(
    x=alt.X('Male:Q', title='Male'),
    y=alt.Y('Age Range:N', sort='-x'),
    color=alt.value('skyblue')
)

chart2 = alt.Chart(data).mark_bar().encode(
    x=alt.X('Female:Q', title='Female'),
    y=alt.Y('Age Range:N', sort='-x'),
    color=alt.value('salmon')
)

# Combine the two charts
chart = alt.hconcat(chart1, chart2)

# Display the chart
chart.show()
