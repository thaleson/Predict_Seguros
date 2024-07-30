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
