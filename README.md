# Air Quality Analysis 🌍

Este projeto tem como objetivo analisar dados ambientais relacionados à **qualidade do ar** e **emissões de CO₂** em diferentes países e regiões. A análise é realizada utilizando **Python**, com processamento de dados feito por **Pandas** e visualizações interativas com **Streamlit**.

## 📌 Descrição

O **Air Quality Analysis** permite:
- Coletar e processar dados de **emissões de CO₂** e **qualidade do ar** a partir de arquivos CSV.
- Realizar limpeza e transformação dos dados em três níveis (Bronze, Silver e Gold).
- Exibir gráficos interativos com informações sobre as emissões de CO₂ por país e a qualidade do ar por região.
- Criar um **dashboard interativo** para facilitar a análise dos dados.

## 🏗️ Arquitetura do Projeto

A estrutura do projeto segue o modelo **Big Data Warehouse (BDW)**, dividido em quatro camadas:

1. **Camada de Ingestão/Recolha de Dados**  
   - Importação de arquivos CSV contendo dados ambientais.  
   
2. **Camada de Armazenamento e Processamento**  
   - **Bronze:** Armazena os dados brutos sem modificações.  
   - **Silver:** Limpeza e normalização dos dados.  
   - **Gold:** Transformação e agregação para análise final.  

3. **Camada de Transformação e Modelação**  
   - Conversão de tipos de dados e tratamento de valores faltantes.  
   - Cálculo da média da qualidade do ar por região e soma total de emissões de CO₂ por país.  

4. **Camada de Visualização**  
   - Construção de um **dashboard interativo** com **Streamlit** para exibir os dados de forma clara e intuitiva.  

## 🚀 Tecnologias Utilizadas

- **Python** 🐍
- **Pandas** 📊
- **Matplotlib & Seaborn** 📈
- **Streamlit** 🖥️
- **Jupyter Notebook** 📝 (para análise exploratória)

## 📊 Funcionalidades

✔️ Gráfico de **Emissões de CO₂ por País (Top 10)**  
✔️ Cálculo da **Média da Qualidade do Ar por Região**  
✔️ Dashboard interativo para visualização dos dados  

⚠️ *Observação:* A análise da qualidade do ar pode apresentar falhas caso os dados disponíveis sejam insuficientes.

## 📁 Estrutura do Repositório

air-quality-analysis/ │── datasets/ # Arquivos CSV contendo os dados ambientais │── src/ # Código-fonte do projeto │ ├── data_processing.py # Processamento e transformação dos dados │ ├── visualization.py # Geração dos gráficos e dashboard │ ├── main.py # Arquivo principal para rodar o projeto │── README.md # Documentação do projeto │── requirements.txt # Bibliotecas necessárias


## ▶️ Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/Andreia797/air-quality-analysis.git
   cd air-quality-analysis
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
3. Execute o dashboard:
   ```bash
   streamlit run src/main.py
4. Acesse o dashboard no navegador pelo link exibido no terminal.

## 📌 Melhorias Futuras
- Adicionar análise temporal para observar a evolução das emissões de CO₂.
- Explorar mais fontes de dados para aumentar a confiabilidade da análise da qualidade do ar.
- Implementar Machine Learning para prever padrões de poluição.

📝 Autor: Andreia Semedo
📅 Última atualização: Março de 2025
