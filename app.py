import streamlit as st
from streamlit_option_menu import option_menu

# Função para carregar o CSS
def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Carregar o CSS
load_css()

# Adicionando um título e uma imagem na sidebar
with st.sidebar:
    st.image("assets/ia.png", width=150)  # Substitua "logo.png" pelo caminho do seu logotipo
    st.markdown("<h1 style='text-align: center;'>Meu Projeto</h1>", unsafe_allow_html=True)
    
    # Definindo o menu lateral com estilo
    selected = option_menu(
        menu_title=None,  # Título do menu é removido, já que temos um título acima
        options=["Home", "About", "Data Visualization", "Model Prediction"],
        icons=["house", "info-circle", "bar-chart", "calculator"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",  # Alinha os itens do menu verticalmente
        styles={
            "container": {"padding": "5px", "background-color": "#f5f5f5"},  # Cor de fundo da sidebar
            "icon": {"color": "black", "font-size": "20px"},  # Cor e tamanho do ícone
            "nav-link": {"font-size": "18px", "text-align": "left", "margin": "5px"},  # Estilo do texto dos links
            "nav-link-selected": {"background-color": "#d6d6d6"},  # Cor de fundo do item selecionado
        }
    )

# Função para chamar a página correspondente
if selected == "Home":
    from pages import home
    home.app()
elif selected == "About":
    from pages import about
    about.app()
elif selected == "Data Visualization":
    from pages import data_visualization
    data_visualization.app()
elif selected == "Model Prediction":
    from pages import model_prediction
    model_prediction.app()
