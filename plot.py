import numpy as np
import pandas as pd 
import streamlit as st
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff

st.header('1. Altair Scatter Plot')
st.write('Altair is a declarative statistical visualization library for Python, based on the Vega and Vega-Lite visualization grammars. It provides a high-level interface for creating interactive visualizations in a concise and expressive manner')
chart_data = pd.DataFrame(np.random.randn(500,5), columns = ['a','b','c','d','e'])
chart = alt.Chart(chart_data).mark_circle().encode(x = 'a' , y = 'b', size = 'c',
        tooltip = ['a','b','c','d','e'])
st.altair_chart(chart)

st.header('2. Interactive Charts')
st.subheader('2.1 Line Chart')
df = pd.read_csv(r"C:\Users\pramo\Desktop\jupyter project\Streamlit\lang_data.csv")
lang_list = df.columns.tolist()
lang_choice = st.multiselect('select your language:',lang_list)
new_df = df[lang_choice]
st.line_chart(new_df)

st.subheader('2.2 Area Chart')
st.area_chart(new_df)

st.header('3. Data Visualisation with Plotly')
st.write('Plotly is a data visualization library that enables users to create interactive and high-quality graphs and charts.')

st.subheader('3.1 Displaying the dataset')
df = pd.read_csv(r"C:\Users\pramo\Desktop\jupyter project\Streamlit\tips.csv")
st.dataframe(df.head())

st.subheader('3.2 Pie Chart')
fig = px.pie(df, values = 'total_bill', names = 'day')
st.plotly_chart(fig)


st.subheader('3.3 Histogram')
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

hist_data = [x1,x2,x3]
group_labels = ['Group - 1', 'Group - 2', 'Group - 3']
fig = ff.create_distplot(hist_data, group_labels, bin_size = [.1,.25,.5])

st.plotly_chart(fig)

