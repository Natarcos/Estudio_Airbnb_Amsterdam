t
import streamlit as st
import pandas as pd
import warnings

from components.header import render_header
from components.footer import render_footer
from components.data_section import display_data_section
from components.eda_section import display_eda_section
from components.ml_section import display_ml_section


warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="🏠 Descubre Amsterdam a través de Airbnb",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

@st.cache_data
def load_data():
    df = pd.read_csv("/Users/n.arcos89/Documents/GitHub/Estudio_Airbnb_Amsterdam/Data/airbnbamsterdam_final_correcto.csv")
    df['last_review'] = pd.to_datetime(df['last_review'])
    df['reviews_per_month'].fillna(0, inplace=True)
    df['last_review'].fillna(pd.Timestamp('1900-01-01'), inplace=True)
    return df

def main():
    render_header()
    df = load_data()

    if df is not None:
        st.sidebar.title("Navegación")
        pages = {
            "📊 Datos": display_data_section,
            "📈 EDA": display_eda_section,
            "🤖 ML Predictor": display_ml_section
        }

        choices = st.sidebar.radio("Selecciona una sección", list(pages.keys()))
        st.sidebar.markdown("---")
        st.sidebar.markdown("### Madrid en un vistazo:")
        st.sidebar.markdown("""
        🎭 **¿Por qué Amsterdam?**
        - Hermosos canales
        - Cultura Vibrante
        - Rica historia
        - Inclusión y diversidad
        """)

        if choices != "🤖 ML Predictor":
            pages[choices](df)
        else:
            pages[choices]()

        render_footer()

if __name__ == "__main__":
    main()