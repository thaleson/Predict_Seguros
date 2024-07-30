import streamlit as st

# Função para carregar o CSS
def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Carregar o CSS
load_css()

# Adicionando conteúdo à sidebar
with st.sidebar:
    st.header("Navegação")
    # Criando uma navegação simples com st.radio
    page = st.radio(
        "Menu:",
        ("Home", "About", "Data Visualization", "Model Prediction")
    )

# Função para chamar a página correspondente
if page == "Home":
    from pages import home
    home.app()
elif page == "About":
    from pages import about
    about.app()
elif page == "Data Visualization":
    from pages import data_visualization
    data_visualization.app()
elif page == "Model Prediction":
    from pages import model_prediction
    model_prediction.app()
