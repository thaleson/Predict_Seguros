
# 🚀 Projeto Predict Seguros

**Predict Seguros** é uma aplicação web desenvolvida com o objetivo de fornecer previsões baseadas em modelos de aprendizado de máquina. O projeto utiliza TensorFlow e Streamlit para criar uma interface interativa e amigável para os usuários.

site : https://predictseguross.streamlit.app/

## 📦 Funcionalidades

- 📊 **Modelagem de Dados:** Treinamento e uso de modelos de aprendizado de máquina.
- 🌐 **Interface Web:** Interface interativa desenvolvida com Streamlit.
- 🔄 **Atualizações Dinâmicas:** Atualizações em tempo real para previsões e resultados.

## 🔧 Tecnologias Utilizadas

- **TensorFlow**: `2.11.0`
- **Keras**: `2.11.0`
- **Streamlit**: `1.37.0`
- **Protobuf**: `3.20.3`
- **NumPy**: `1.24.4`
- **Pandas**: `2.0.3`
- **Scikit-Learn**: `1.3.2`
- **Matplotlib**: `3.7.5`
- **Seaborn**: `0.13.2`
- **Requests**: `2.32.3`

## 💻 Instalação

Siga os passos abaixo para instalar e configurar o projeto:

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/thaleson/Predict_Seguross
   cd predict-seguros
   ```

2. **Crie um Ambiente Virtual**

   Para garantir que todas as dependências sejam gerenciadas adequadamente, é recomendável usar um ambiente virtual. Você pode criar um usando `venv` ou `virtualenv`.

   ```bash
   python -m venv venv
   ```

   Ative o ambiente virtual:

   - **Windows:**

     ```bash
     .\venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

3. **Instale as Dependências**

   Com o ambiente virtual ativado, instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Executando a Aplicação

Para iniciar a aplicação, execute o seguinte comando:

```bash
streamlit run app.py
```

A aplicação será iniciada e poderá ser acessada em [http://localhost:8501](http://localhost:8501).

## 🛠️ Estrutura do Projeto

- `app.py`: Arquivo principal para execução da aplicação.
- `pages/`: Diretório contendo os arquivos das páginas da aplicação.
- `modelos/`: Diretório contendo os modelos treinados.
- `requirements.txt`: Lista de dependências do projeto.

## 📝 Contribuindo

Contribuições são bem-vindas! Se você deseja contribuir para o projeto, siga estes passos:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nome-da-feature`).
3. Faça commit das suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Envie para o repositório remoto (`git push origin feature/nome-da-feature`).
5. Crie um Pull Request.

## 📝 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Sinta-se à vontade para personalizar o README conforme necessário e adicione qualquer informação específica do projeto que julgar importante.
