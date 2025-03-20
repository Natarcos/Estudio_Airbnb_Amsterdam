import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

def display_eda_section(df: pd.DataFrame):
    st.header("📈 Análisis Exploratorio")

    # Distribución de Precios
    st.subheader("Distribución de Precios")
    fig = px.histogram(df, x="price", nbins=50, title="Histograma de Precios")
    st.plotly_chart(fig, use_container_width=True)

    # Barrios en los que se concentran los alojamientos
    st.subheader("Barrios en los que se concentran los alojamientos")
    neighborhood_counts = df['neighbourhood'].value_counts().reset_index()
    neighborhood_counts.columns = ['neighbourhood', 'count']

    # Agrupar barrios con pocos alojamientos en "Otros"
    threshold = 0.01  # Umbral para agrupar en "Otros"
    total_count = neighborhood_counts['count'].sum()
    neighborhood_counts['percentage'] = neighborhood_counts['count'] / total_count
    neighborhood_counts.loc[neighborhood_counts['percentage'] < threshold, 'neighbourhood'] = 'Otros'
    neighborhood_counts = neighborhood_counts.groupby('neighbourhood').sum().reset_index()

    fig = px.pie(neighborhood_counts, values='count', names='neighbourhood', title='Distribución de Alojamientos por Barrio')
    st.plotly_chart(fig, use_container_width=True)

    # Relación entre Precio y Barrio
    st.subheader("Variación de los precios por barrios")
    fig = px.bar(df, x="neighbourhood", y="price", color="neighbourhood",
                labels={"neighbourhood": "Barrio", "price": "Precio por Noche"},
                hover_data=["price"])
    st.plotly_chart(fig, use_container_width=True)

    # Relación entre Precio y Tipo de Habitación
    st.subheader("Precio medio según el tipo de habitación")
    # Asegúrate de que no hay valores nulos en las columnas 'room_type' y 'price'
    df_filtered = df.dropna(subset=['room_type', 'price'])
    avg_price_by_room_type = df_filtered.groupby('room_type')['price'].mean().reset_index()
    avg_price_by_room_type.columns = ['room_type', 'avg_price']

    fig = px.scatter(avg_price_by_room_type, x="room_type", y="avg_price", size="avg_price", color="room_type",
                    title="Precio Medio de Alojamientos por Tipo de Habitación",
                    labels={"room_type": "Tipo de Habitación", "avg_price": "Precio Medio"},
                    size_max=60)
    st.plotly_chart(fig, use_container_width=True)

    # Relación entre Precio y Número de Reseñas
    st.subheader("Relación entre Precio y Número de Reseñas")
    # Asegúrate de que no hay valores nulos en las columnas 'price' y 'number_of_reviews'
    df_filtered_reviews = df.dropna(subset=['price', 'number_of_reviews'])
    fig = px.density_heatmap(df_filtered_reviews, x="number_of_reviews", y="price", nbinsx=30, nbinsy=30,
                            title="Relación entre Precio y Número de Reseñas",
                            labels={"number_of_reviews": "Número de Reseñas", "price": "Precio"})
    st.plotly_chart(fig, use_container_width=True)

    # Matriz de Correlación
    st.subheader("Matriz de Correlación")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr = df[numeric_cols].corr()
    fig_corr = px.imshow(corr, text_auto=True, aspect="auto", title="Correlaciones")
    st.plotly_chart(fig_corr, use_container_width=True)