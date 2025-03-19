import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

def display_eda_section(df: pd.DataFrame):
    st.header("📈 Análisis Exploratorio")
    
    st.subheader("Distribución de Precios")
    fig = px.histogram(df, x="price", nbins=50, title="Histograma de Precios")
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Barrios en los que se concentran los alojamientos")
    neighborhood_counts = df['neighbourhood'].value_counts().reset_index()
    neighborhood_counts.columns = ['neighbourhood', 'count']
    
    # Agrupar barrios con pocos alojamientos en "Otros"
    threshold = 0.01  # Umbral para agrupar en "Otros"
    total_count = neighborhood_counts['count'].sum()
    neighborhood_counts['percentage'] = neighborhood_counts['count'] / total_count
    neighborhood_counts.loc[neighborhood_counts['percentage'] < threshold, 'neighbourhood'] = 'Otros'
    neighborhood_counts = neighborhood_counts.groupby('neighbourhood').sum().reset_index()
    
    fig = px.pie(neighborhood_counts, values='count', names='neighbourhood')
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Variación de los precios por barrios")
    fig = px.scatter(df, x="neighbourhood", y="price", color="neighbourhood")
                    labels={"neighbourhood": "Barrio", "price": "Precio"},
                    hover_data=["price"])
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Matriz de Correlación")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr = df[numeric_cols].corr()
    fig_corr = px.imshow(corr, text_auto=True, aspect="auto", title="Correlaciones")
    st.plotly_chart(fig_corr, use_container_width=True)