import streamlit as st

def app():
    st.title('Previsão de Seguros')
    st.markdown('''
    Bem-vindo ao sistema de previsão de seguros! 
    Use este aplicativo para prever o valor do seguro com base em diferentes variáveis.

    Para saber mais sobre como nosso modelo funciona, visite as outras páginas.
    ''')
    st.markdown('### Comprar Seguro')
    st.image('https://modesttipittolseguros.com.br/uploads/images/183-256-orig.jpg?=v1', caption='Imagem de Seguro')
