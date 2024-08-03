import streamlit as st
from streamlit_option_menu import option_menu
import time  # Importado para simular o carregamento

# Configuração da página principal
st.set_page_config(page_title="Predictseguros", page_icon="🛡️")

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
    from pages.separador import home
    home.app()

elif selected == "About":
    from pages.separador import about
    about.app()

elif selected == "Data Visualization":
    from pages.separador import data_visualization
    data_visualization.app()

elif selected == "Model Prediction":
    from pages.separador import model_prediction

    # Função de previsão com carregamento
    def run_prediction(input1, input2, input3):
        with st.spinner("Calculando a previsão, por favor aguarde..."):
            time.sleep(2)  # Simula o tempo de carregamento
            # Aqui você chamaria a função real de previsão com os inputs fornecidos
            result = model_prediction.predict(input1, input2, input3)
            st.success(f"A previsão é: {result}")

    # Interface para a página Model Prediction
    st.header("Previsão do Modelo")
    st.info("Preencha os campos abaixo e clique em 'Prever' para realizar a previsão.")

    # Inputs com valores zerados e descrições claras
    valor1 = st.number_input("Valor de Entrada 1", value=0, help="Insira o valor para a variável 1. Exemplo: 5")
    valor2 = st.number_input("Valor de Entrada 2", value=0, help="Insira o valor para a variável 2. Exemplo: 10")
    valor3 = st.number_input("Valor de Entrada 3", value=0, help="Insira o valor para a variável 3. Exemplo: 20")

    # Botão para realizar a previsão
    if st.button("Prever"):
        run_prediction(valor1, valor2, valor3)
