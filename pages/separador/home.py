import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def app():
    st.title('Previsão de Seguros')
    st.markdown('''
    Bem-vindo ao sistema de previsão de seguros! 
    Use este aplicativo para prever o valor do seguro com base em diferentes variáveis.

    Para saber mais sobre como nosso modelo funciona, visite as outras páginas.
    ''')

    st.markdown('### Comprar Seguro')
    st.image('https://modesttipittolseguros.com.br/uploads/images/183-256-orig.jpg?=v1', caption='Imagem de Seguro')

    # URL da animação Lottie em JSON
    lottie_url = 'https://lottiefiles.com/free-animation/laptop-icon-lottie-json-animation-xujxtfROo8'
    lottie_animation = load_lottie_url(lottie_url)

    if lottie_animation:
        st_lottie(lottie_animation, speed=1, width=700, height=400, key="animation")

    # Link para o LinkedIn
    st.markdown('''
    <hr>
    <div style='text-align: center;'>
        <p>Site desenvolvido por Thaleson Silva</p>
        <a href='https://www.linkedin.com/in/thaleson-silva-9298a0296/' target='_blank'>
            <button style='background-color: #0073b1; color: white; padding: 10px; border: none; border-radius: 5px;'>
                LinkedIn
            </button>
        </a>
    </div>
    ''', unsafe_allow_html=True)
