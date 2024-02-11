import pandas as pd
import plotly.graph_objects as go

# Load the data from the CSV file
df = pd.read_csv('pyramiddata.csv')

# Create the bullet chart
fig = go.Figure()

for _, row in df.iterrows():
    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta",
        gauge = {'shape': "bullet"},
        delta = {'reference': row['Female']},
        value = row['Male'],
        domain = {'x': [0, 1], 'y': [row.name/len(df), (row.name+1)/len(df)]},
        title = {'text': row['Age Range']}
    ))

# Show the plot
fig.show()
