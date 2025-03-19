# filepath: /Users/n.arcos89/Documents/GitHub/Estudio_Airbnb_Amsterdam/Components/ml_section.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

def display_ml_section():
    st.header("🤖 Planifica tu Presupuesto - Predicción de Precios")

    # Cargar modelo, scaler y columnas
    model_path = "Models/airbnb_model.pkl"
    scaler_path = "Models/scaler.pkl"
    feature_names_path = "Models/features_names.pkl"

    if not os.path.exists(model_path):
        st.error(f"El archivo del modelo no se encontró en la ruta: {model_path}")
        return
    if not os.path.exists(scaler_path):
        st.error(f"El archivo del scaler no se encontró en la ruta: {scaler_path}")
        return
    if not os.path.exists(feature_names_path):
        st.error(f"El archivo de nombres de características no se encontró en la ruta: {feature_names_path}")
        return

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    feature_names = joblib.load(feature_names_path)

    st.markdown("""
    Ajusta los parámetros de tu alojamiento ideal y obtén una estimación del precio.
    """)

    # Inputs de usuario
    room_type = st.selectbox("Tipo de habitación", ["Entire home/apt","Private room","Shared room","Hotel room"])
    minimum_nights = st.number_input("Noches Mínimas", min_value=1, max_value=365, value=2)
    number_of_reviews = st.number_input("Número de Reviews", min_value=0, value=0)
    reviews_per_month = st.number_input("Reviews por Mes", min_value=0.0, value=1.0)
    host_listings = st.number_input("Número de Listings del Anfitrión", min_value=1, value=1)
    availability_365 = st.number_input("Disponibilidad (días)", min_value=0, max_value=365, value=180)

    if st.button("Predecir"):
        input_data = {
            "minimum_nights": [minimum_nights],
            "number_of_reviews": [number_of_reviews],
            "reviews_per_month": [reviews_per_month],
            "calculated_host_listings_count": [host_listings],
            "availability_365": [availability_365],
            "room_type": [room_type]
        }
        input_df = pd.DataFrame(input_data)

        # One-hot encoding para 'room_type'
        input_encoded = pd.get_dummies(input_df, columns=["room_type"])

        # Rellenar columnas faltantes y mantener orden
        for col in feature_names:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        input_encoded = input_encoded[feature_names]

        # Escalar
        input_scaled = scaler.transform(input_encoded)

        # Predicción
        pred_price = model.predict(input_scaled)[0]
        st.success(f"El precio estimado por noche es: ${pred_price:.2f}")