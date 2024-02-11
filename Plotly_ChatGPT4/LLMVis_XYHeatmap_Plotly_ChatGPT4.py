import pandas as pd
import plotly.express as px

# Load the data from the CSV file
df = pd.read_csv('heatmapDataOrig.csv')

# Create the XY Heatmap chart
fig = px.density_heatmap(df, x='A', y='B', z='C')

# Show the plot
fig.show()
