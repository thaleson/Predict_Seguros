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

    # Campos de entrada para os dados com descrições mais amigáveis
    st.subheader("Dados para Previsão")
    
    input_data = {
        "Média Avaliada pelo Cliente": st.number_input("Insira a média avaliada pelo cliente", value=0.0, format="%.2f", help="Média que o cliente avaliou para o seguro, ex: 1500.00"),
        "Seguro Internacional (sim/não)": st.selectbox("Inclui Seguro Internacional?", options=["Sim", "Não"]),
        "Cobertura Odontológica (sim/não)": st.selectbox("Inclui Cobertura Odontológica?", options=["Sim", "Não"]),
        "Cobertura para Pessoas Acima de 65 Anos (sim/não)": st.selectbox("Inclui Cobertura para Pessoas Acima de 65 Anos?", options=["Sim", "Não"]),
        "Reembolso de Despesas Médicas (em R$)": st.number_input("Insira o valor de reembolso de despesas médicas", value=0.0, format="%.2f", help="Valor do reembolso para despesas médicas, ex: 500.00"),
        "Cobertura para Esportes Radicais (sim/não)": st.selectbox("Inclui Cobertura para Esportes Radicais?", options=["Sim", "Não"]),
        "Capital Segurado (em R$)": st.number_input("Insira o capital segurado", value=0.0, format="%.2f", help="Valor total do capital segurado, ex: 20000.00"),
        "Inclui Bônus (sim/não)": st.selectbox("Inclui Bônus?", options=["Sim", "Não"]),
        "Valor Unitário (em R$)": st.number_input("Insira o valor unitário", value=0.0, format="%.2f", help="Valor unitário do seguro, ex: 1000.00"),
    }

    # Transformando os dados de entrada em formato adequado
    input_values = np.array([[value if isinstance(value, (int, float)) else (1 if value == "Sim" else 0) for value in input_data.values()]])
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
