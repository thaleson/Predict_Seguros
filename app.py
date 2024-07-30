import streamlit as st
from streamlit_option_menu import option_menu


# Função para carregar o CSS
def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Carregar o CSS
load_css()

# Definindo o menu lateral no início da sidebar
with st.sidebar:
    st.header("Meu Projeto")  # Título ou nome do projeto

    # Menu de opções
    selected = option_menu(
        menu_title="",  # Título do menu vazio para ocupar menos espaço
        options=["Home", "About", "Data Visualization", "Model Prediction"],
        icons=["house", "info-circle", "bar-chart", "calculator"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
    )

# Função para chamar a página correspondente
if selected == "Home":

    from pages.separador import home, model_prediction, about, data_visualization

    home.app()
elif selected == "About":
    from pages.separador import about

    about.app()

elif selected == "Data Visualization":
    from pages.separador import data_visualization

    data_visualization.app()
elif selected == "Model Prediction":
    from pages.separador import model_prediction

    model_prediction.app()
