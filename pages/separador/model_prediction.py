import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import time  # Importado para simular o carregamento

def app():
    st.title("Previsão de Seguros")
    st.write("Insira os dados abaixo para obter uma previsão do valor do seguro:")

    # Carregando os dados para obter a escala (ajuste o caminho conforme necessário)
    data = pd.read_csv("dataset/vendas_data_training.csv")
    X = data.drop(columns=['total_vendas'])
    Y = data['total_vendas']

    X_scaler = MinMaxScaler()
    X_scaler.fit(X)

    # Campos de entrada para os dados
    input_data = {col: st.number_input(col, value=0.0) for col in X.columns}

    # Transformando os dados de entrada em formato adequado
    input_values = np.array([[value for value in input_data.values()]])
    input_values_scaled = X_scaler.transform(input_values)

    if st.button("Prever"):
        # Verifica se todos os inputs são zero e exibe uma mensagem de erro se necessário
        if np.all(input_values == 0):
            st.error("Por favor, informe os dados corretamente.", icon="🚨")
        else:
            # Simula o tempo de carregamento
            with st.spinner("Calculando a previsão, por favor aguarde..."):
                time.sleep(2)  # Simula o tempo de carregamento
                # Carrega o modelo e faz a previsão
                model = tf.keras.models.load_model("modelos/modelo_treinado_v3.h5")
                prediction = model.predict(input_values_scaled)
                st.success(f"Previsão do Valor do Seguro: R$ {prediction[0][0]:.2f}")
