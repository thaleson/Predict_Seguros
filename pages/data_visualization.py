import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.title("Visualização de Dados")
    st.markdown("Aqui você pode explorar visualmente o conjunto de dados utilizado no treinamento do modelo.")

    # Carregando dados (substitua pelo caminho correto ou carregue diretamente de uma fonte de dados)
    data = pd.read_csv("dataset/vendas_data_test.csv")

    st.write("Visualização de amostra dos dados:")
    st.write(data.head())

    # Gráfico de dispersão
    st.write("Gráfico de dispersão entre características:")
    feature_x = st.selectbox("Selecione a característica para o eixo X", data.columns)
    feature_y = st.selectbox("Selecione a característica para o eixo Y", data.columns)

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=feature_x, y=feature_y)
    st.pyplot(plt)
