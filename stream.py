import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def makeplot(dataframe, par1="цена", par2="штуки", color1="#e695cb", color2="#1db8cc"):
  fig = make_subplots(specs=[[{"secondary_y": True}]])
  fig.add_trace(
    go.Scatter(x=dataframe['период'], y=dataframe[par1].fillna(method='backfill'), name=par1),
    secondary_y=False
  )
  fig.add_trace(
    go.Scatter(x=dataframe['период'], y=dataframe[par2].fillna(method='backfill'), name=par2),
    secondary_y=True
  )

  fig.update_layout(
    title_text=""
  )

  fig['data'][0]['line']['color']=color1
  fig['data'][0]['line']['width']=3
  fig['data'][1]['line']['color']=color2
  fig['data'][1]['line']['width']=3


  fig.update_xaxes(title_text="")


  fig.update_yaxes(title_text="<b>"+par1+"</b>", secondary_y=False)
  fig.update_yaxes(title_text="<b>"+par2+"</b>", secondary_y=True)

  fig.update_yaxes(showgrid=False, gridwidth=1, gridcolor='Grey', griddash='dot')
  fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='Grey', griddash='dot')
  fig.update_layout(plot_bgcolor = "#f7f7f7")
  

  fig.show()

st.title('Генератор графиков')

st.markdown('''
    Загружать файлы можно в формате csv
''')

uploaded_file = st.file_uploader('Загрузить файл', type='csv')
if (uploaded_file is not None):
    df = pd.read_csv(uploaded_file)
    st.markdown('success')
    makeplot(df, par2="оборот")
    makeplot(df, par2="штуки")