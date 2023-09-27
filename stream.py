import pandas as pd
import streamlit as st



st.title('Генератор графиков')

st.markdown('''
    Загружать файлы можно в формате csv
''')

uploaded_file = st.file_uploader('Загрузить файл', type='csv')
if (uploaded_file is not None):
    st.markdown('success')