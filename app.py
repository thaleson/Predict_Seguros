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
  
    
    # Definindo o menu lateral com estilo
    selected = option_menu(
        menu_title="Menu",  
          ('Home', 'About', 'Data Visualization', 'Model Prediction')
     
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
