import pandas as pd
import plotly.express as px

# Load the data from the CSV file
df = pd.read_csv('mycarsUnique.csv')

# Create the grouped column chart
fig = px.bar(df, x='Name', y='Price', color='Type', barmode='group')

# Show the plot
fig.show()
