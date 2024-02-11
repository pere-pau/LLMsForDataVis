# Import necessary libraries
import altair as alt
import pandas as pd

# Load the data from CSV file
data = pd.read_csv('myfileDotPlot2Values.csv')

# Convert column 'B' into two separate columns 'B_lower' and 'B_upper'
data[['B_lower', 'B_upper']] = pd.DataFrame(data['B'].tolist(), index=data.index)

# Create a range plot
chart = alt.Chart(data).mark_rule().encode(
    x='B_lower:Q',
    x2='B_upper:Q',
    y='A:N'
)

# Display the chart
chart.show()
