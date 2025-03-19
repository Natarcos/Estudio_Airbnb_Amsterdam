import streamlit as st

def render_header():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title("Descubre Amsterdam a través de Airbnb")
        st.markdown("""
        Bienvenido al análisis oficial de alojamientos turísticos en Amsterdam. 
        Explora la ciudad de los canales a través de los datos de Airbnb.
                    
        Una iniciativa del Departamento de Turismo de Amsterdam y Airbnb.
        """)
        st.markdown("---")
                