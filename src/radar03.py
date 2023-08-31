import plotly.express as px
import pandas as pd

# $ pip install -U kaleido


# # Datos de muestra
# df = pd.DataFrame(dict(
#     valor = [8, 12, 7, 14, 10],
#     variable = ['V1', 'V2', 'V3', 'V4', 'V5']))
           
# fig = px.line_polar(df, r = 'valor', theta = 'variable', line_close = True,
#                     markers = True)

# fig.show() 
import os
import sys

import plotly.graph_objects as go
import plotly.offline as pyo

os.chdir("/home/eduardo/GCBA/Encuesta/")


df = pd.read_csv('Score_Final.csv',sep=';', encoding='utf-8')
df2 = df.drop(['Area'], axis=1)
df3 = df2.drop(['Organismo'], axis=1)

categories = [*df3.columns[0:], df3.columns[0]]
#categories2 = categories.pop(0)
#categories.remove("Organismo")
#categories.remove("Organismo")

data = [go.Scatterpolar(
            r=[*row.values, row.values[0]],
            theta=categories,
            name=label) for label, row in df3.iterrows()]

fig = go.Figure(
    data=data,
    layout=go.Layout(
        title=go.layout.Title(text="Análisis de Dimensiones", xanchor='center', x=0.2),
        polar={'radialaxis': {'visible': True}},
        showlegend=True
    )
)
fig.update_traces(fill = 'toself')
pyo.plot(fig)
fig.write_image("radar01.png")