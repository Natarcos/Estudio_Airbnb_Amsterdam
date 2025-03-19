import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

def display_eda_section(df: pd.DataFrame):
    st.header("📈 Análisis Exploratorio")
    
    st.subheader("Distribución de Precios")
    fig = px.histogram(df, x="price", nbins=50, title="Histograma de Precios")
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Matriz de Correlación")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr = df[numeric_cols].corr()
    fig_corr = px.imshow(corr, text_auto=True, aspect="auto", title="Correlaciones")
    st.plotly_chart(fig_corr, use_container_width=True)