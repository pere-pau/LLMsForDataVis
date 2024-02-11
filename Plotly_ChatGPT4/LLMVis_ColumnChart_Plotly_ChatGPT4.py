import pandas as pd
import plotly.express as px

# Load the data from the CSV file
df = pd.read_csv('myfile.csv')

# Create the column chart
fig = px.bar(df, x='A', y='B')

# Show the plot
fig.show()
