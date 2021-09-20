import pandas as pd
import plotly.express as px

df = pd.read_csv("line_chart.csv")
fig = px.line(df, x="Population", y="Per capita", color="Country", size="Percentage", size_max=60)
fig.show()