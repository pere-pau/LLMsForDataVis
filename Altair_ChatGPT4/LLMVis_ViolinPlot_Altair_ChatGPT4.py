# Import necessary libraries
import altair as alt
from vega_datasets import data
import pandas as pd

# Load the data from CSV file
data = pd.read_csv('myfileDotPlot.csv')

# Create a violin plot
chart = alt.Chart(data).transform_density(
    'B',
    as_=['B', 'density'],
    groupby=['A']
).mark_area(orient='horizontal').encode(
    y='B:Q',
    color='A:N',
    x=alt.X(
        'density:Q',
        stack='center',
        impute=None,
        title=None,
        axis=alt.Axis(labels=False, values=[0],grid=False, ticks=True),
    ),
    column='A:N'
).properties(
    width=100
).configure_facet(
    spacing=0
).configure_view(
    stroke=None
)

# Display the chart
chart.show()
