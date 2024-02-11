import pandas as pd
import plotly.express as px

# Load the data from the CSV file
df = pd.read_csv('mycarsUnique.csv')

# Create the stacked bar chart
fig = px.bar(df, x='Name', y='Price', color='Type', barmode='stack')

# Show the plot
fig.show()
