import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

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
        model = tf.keras.models.load_model("modelos/modelo_treinado_v3.h5")
        prediction = model.predict(input_values_scaled)
        st.write(f"Previsão do Valor do Seguro: {prediction[0][0]:.2f}")

