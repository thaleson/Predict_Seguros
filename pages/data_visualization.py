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

    # Gráfico de barras
    st.write("Gráfico de barras da contagem de valores de uma característica:")
    feature = st.selectbox("Selecione a característica para o gráfico de barras", data.columns)

    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x=feature)
    plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x se necessário
    st.pyplot(plt)
