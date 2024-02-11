import pandas as pd
import plotly.express as px

# Load the data from the CSV file
df = pd.read_csv('myfile.csv')

# Create the pie chart
fig = px.pie(df, names='A', values='B')

# Show the plot
fig.show()



