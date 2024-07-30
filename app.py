import streamlit as st

# Função para carregar o CSS
def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Carregar o CSS
load_css()

# Adicionando o nome do app e as rotas na sidebar
with st.sidebar:
    st.header("Meu Projeto")
    
    # Links para as páginas
    if st.button("Home"):
        from pages import home
        home.app()
    if st.button("About"):
        from pages import about
        about.app()
    if st.button("Data Visualization"):
        from pages import data_visualization
        data_visualization.app()
    if st.button("Model Prediction"):
        from pages import model_prediction
        model_prediction.app()
