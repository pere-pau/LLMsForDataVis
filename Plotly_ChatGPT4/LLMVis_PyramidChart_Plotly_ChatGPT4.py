import pandas as pd
import plotly.graph_objects as go


# Load the data from the CSV file
df = pd.read_csv('pyramiddata.csv')

# Create the pyramid chart
fig = go.Figure()

fig.add_trace(go.Bar(
    y=df['Age Range'],
    x=df['Male'],
    name='Male',
    orientation='h',
    marker=dict(color='blue')
))

fig.add_trace(go.Bar(
    y=df['Age Range'],
    x=-df['Female'],
    name='Female',
    orientation='h',
    marker=dict(color='red')
))

fig.update_layout(barmode='relative', title_text='Pyramid Chart')

# Show the plot
fig.show()
