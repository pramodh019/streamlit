import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

chart_data = pd.DataFrame(np.random.randn(20,3),  columns = ['Line-1','Line-2','Line-3'])

st.header('1. Charts with random numbers')

st.subheader('1.1 Line Chart')
st.line_chart(chart_data)

st.subheader('1.2 area chart')
st.area_chart(chart_data)

st.subheader('1.3 bar Chart')
st.bar_chart(chart_data)


st.header('2. Visualization with Matplotlib & Seaborn')

st.subheader('2.1 Loading the DataFrame')
df = pd.read_csv(r"C:\Users\pramo\Desktop\jupyter project\Streamlit\iris.csv")
st.table(df.head(n=10))

st.header('bar chart')
fig= plt.figure(figsize = (15,8))
df['species'].value_counts().plot(kind = 'bar')
st.pyplot(fig)

st.header('line chart')
fig= plt.figure(figsize = (15,8))
df['petal_length'].value_counts().plot(kind = 'line')
st.pyplot(fig)

st.header('area chart')
fig= plt.figure(figsize = (15,8))
df['sepal_length'].value_counts().plot(kind = 'area')
st.pyplot(fig)


st.header('hist chart')
fig= plt.figure(figsize = (15,8))
df['sepal_width'].value_counts().plot(kind = 'hist')
st.pyplot(fig)

st.header('box chart')
fig= plt.figure(figsize = (15,8))
df['sepal_length'].value_counts().plot(kind = 'box')
st.pyplot(fig)

st.header('pie chart')
fig= plt.figure(figsize = (15,8))
df['species'].value_counts().plot(kind = 'pie')
st.pyplot(fig)

st.header('3. Multiple Graphs in one columns')
col1, col2 = st.columns(2)
with col1:
    col1.header= 'KDE=False'
    fig1=plt.figure(figsize=(5,5))
    sns.distplot(df['sepal_length'], kde = False)
    st.pyplot(fig1)
with col2:
    col2.header = 'Hist = False'
    fig2 = plt.figure(figsize = (5,5))
    sns.distplot(df['sepal_length'], hist = False)
    st.pyplot(fig2)

st.header('4. Changing Style')
col1, col2 = st.columns(2)
with col1:
    fig = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['petal_length'], hist = False)
    st.pyplot(fig)
with col2:
    fig = plt.figure()
    sns.set_theme(context = 'poster', style = 'darkgrid')
    sns.distplot(df['petal_length'], hist = False)
    st.pyplot(fig)


