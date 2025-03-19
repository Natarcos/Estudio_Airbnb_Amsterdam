import streamlit as st

def render_footer():
    st.markdown("---")
    st.markdown(
        """
        <div.style='text-align:center,color:#666,'>
        <p>Desarrollado por el Departamento de Turismo de Amsterdam y Airbnb | © 2025 Ayuntamiento de Amsterdam</p>
            <p>¿Necesitas más información? Visita
               <a href="https://amsterdam.org/en/">amsterdam.org</a> o
               contacta con nuestras oficinas de turismo.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )