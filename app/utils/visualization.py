import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st

# Função para criar gráfico de barras
def create_bar_chart(data, x, y, title, labels, color):
    fig = px.bar(
        data,
        x=x,
        y=y,
        title=title,
        labels=labels,
        color=color,
        color_continuous_scale='Blues'
    )
    st.plotly_chart(fig)

# Função para criar Word Cloud
def create_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

# Função para criar gráfico de linha
def create_line_chart(data, x, y, title, labels):
    fig = px.line(
        data,
        x=x,
        y=y,
        title=title,
        labels=labels
    )
    st.plotly_chart(fig)