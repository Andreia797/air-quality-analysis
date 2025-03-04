import os
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def load_data(emissoes_path, qualidade_path):
    if not os.path.exists(emissoes_path) or not os.path.exists(qualidade_path):
        st.error("❌ Arquivos de dados não encontrados. Execute o script de processamento de dados primeiro.")
        return None, None
    df_emissoes = pd.read_csv(emissoes_path)
    # Lê o CSV de qualidade do ar sem cabeçalho e define os nomes das colunas
    df_qualidade = pd.read_csv(qualidade_path, sep=";", header=None,
                                 names=["Col1", "Pollutant", "Source", "Unit", "SomeValue", "Timestamp", "Region"],
                                 encoding="utf-8-sig")
    st.markdown("#### Dados brutos de Qualidade do Ar:")
    st.write(df_qualidade.head())
    st.write("Shape:", df_qualidade.shape)
    return df_emissoes, df_qualidade

def process_data(df_emissoes, df_qualidade):
    # Processamento do dataset de emissões
    if "Area" in df_emissoes.columns:
        df_emissoes.rename(columns={"Area": "Country"}, inplace=True)
    
    # Identificar colunas que representam anos e somar os valores para criar a coluna 'Emissions'
    colunas_anos = [col for col in df_emissoes.columns if col.isdigit()]
    if colunas_anos:
        df_emissoes["Emissions"] = df_emissoes[colunas_anos].sum(axis=1)
    
    # Nesta abordagem, usamos a coluna "SomeValue" como a medida de qualidade do ar.
    # Converte a coluna SomeValue para numérico
    df_qualidade["AirQuality"] = pd.to_numeric(
        df_qualidade["SomeValue"].astype(str).str.replace(",", ".").str.strip(), errors="coerce"
    )
    
    st.markdown("#### Valores de AirQuality (convertidos a partir de SomeValue):")
    st.write(df_qualidade["AirQuality"].head(10))
    st.write("Tipo:", df_qualidade["AirQuality"].dtype)
    st.write("Valores únicos:", df_qualidade["AirQuality"].unique())
    
    return df_emissoes, df_qualidade

def analyze_data(df_emissoes, df_qualidade):
    top_emissions = df_emissoes.groupby("Country")["Emissions"].sum().sort_values(ascending=False).head(10)
    
    df_qualidade_clean = df_qualidade.dropna(subset=["AirQuality"])
    st.markdown("#### Número de registros com AirQuality válido:")
    st.write(len(df_qualidade_clean))
    
    air_quality_avg = df_qualidade_clean.groupby("Region")["AirQuality"].mean()
    return top_emissions, air_quality_avg

def dashboard():
    st.title("📊 Dashboard: Qualidade do Ar e Emissões de CO₂")
    
    caminho_emissoes = "datasets/emissoes_limpo.csv"
    caminho_qualidade = "datasets/qualidade_ar_limpo.csv"
    
    df_emissoes, df_qualidade = load_data(caminho_emissoes, caminho_qualidade)
    if df_emissoes is None or df_qualidade is None:
        return
    
    st.markdown("### Dados de Emissões (Amostra):")
    st.write(df_emissoes.head())
    
    st.markdown("### Dados de Qualidade do Ar (Amostra):")
    st.write(df_qualidade.head())
    
    df_emissoes, df_qualidade = process_data(df_emissoes, df_qualidade)
    top_emissions, air_quality_avg = analyze_data(df_emissoes, df_qualidade)
    
    st.subheader("🌍 Emissões de CO₂ por País (Top 10)")
    fig_emissoes, ax_emissoes = plt.subplots(figsize=(10, 5))
    top_emissions.plot(kind="bar", ax=ax_emissoes, color="red")
    ax_emissoes.set_xlabel("País")
    ax_emissoes.set_ylabel("Emissões (kilotonnes)")
    ax_emissoes.set_title("Top 10 Países por Emissões")
    st.pyplot(fig_emissoes)
    
    st.subheader("🌎 Média da Qualidade do Ar por Região")
    if not air_quality_avg.empty:
        fig_qualidade, ax_qualidade = plt.subplots(figsize=(10, 5))
        air_quality_avg.plot(kind="bar", ax=ax_qualidade, color="blue")
        ax_qualidade.set_xlabel("Região")
        ax_qualidade.set_ylabel("Qualidade do Ar (Média)")
        ax_qualidade.set_title("Média da Qualidade do Ar")
        st.pyplot(fig_qualidade)
    else:
        st.warning("⚠️ Não há dados válidos para gerar o gráfico de qualidade do ar.")
    
    st.markdown("#### Dados obtidos de fontes públicas e processados com Python.")

if __name__ == "__main__":
    dashboard()
