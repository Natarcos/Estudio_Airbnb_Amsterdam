import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import folium_static

def display_data_section(df: pd.DataFrame):
    st.header("📊 Amsterdam en Números")
    st.markdown("""Algunos datos generales de la oferta de Airbnb en Amsterdam...""")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Alojamientos Disponibles", f"{len(df):,}")
    with col2:
        st.metric("Precio Promedio/Noche", f"${df['price'].mean():.2f}")
    with col3:
        st.metric("Anfitriones Únicos", f"{df['host_id'].nunique():,}")
    with col4:
        st.metric("Reviews Promedio", f"{df['number_of_reviews'].mean():.1f}")

    st.markdown("---")
    
    # Mapa de ejemplo
    sample_df = df.head(100)
    m = folium.Map(location=[sample_df['latitude'].mean(), sample_df['longitude'].mean()], zoom_start=12)
    for idx, row in sample_df.iterrows():
        folium.Marker([row['latitude'], row['longitude']], 
                      popup=f"{row['neighbourhood']} - ${row['price']}"
                     ).add_to(m)
    folium_static(m)