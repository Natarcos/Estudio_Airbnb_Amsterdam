import streamlit as st
import pandas as pd
import numpy as np
import joblib


def display_ml_section():
    st.header("🤖 Planifica tu Presupuesto - Predicción de Precios")

    # Cargar modelo, scaler y columnas
    model = joblib.load("models/airbnb_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    feature_names = joblib.load("models/features_names.pkl")

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