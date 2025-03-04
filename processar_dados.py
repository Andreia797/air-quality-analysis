import pandas as pd
import os

# Definir caminhos dos arquivos CSV
caminho_emissoes = "C:/Users/Andreia/Ambiente de Trabalho/Andreia/AndreiaEIC/1º Simestre/CD-2025/Trabalho/TrabalhoBigData/datasets/total_emissions_per_country.csv"
caminho_qualidade_ar = "C:/Users/Andreia/Ambiente de Trabalho/Andreia/AndreiaEIC/1º Simestre/CD-2025/Trabalho/TrabalhoBigData/datasets/world_air_quality_data.csv"

# Tentar carregar os dados com verificação de erro
try:
    df_emissoes = pd.read_csv(caminho_emissoes)
    print("✅ Dados de Emissões carregados com sucesso!")
except Exception as e:
    print(f"❌ Erro ao carregar {caminho_emissoes}: {e}")

try:
    df_qualidade_ar = pd.read_csv(caminho_qualidade_ar, on_bad_lines="skip", encoding="utf-8")
    print("✅ Dados de Qualidade do Ar carregados com sucesso!")
except Exception as e:
    print(f"❌ Erro ao carregar {caminho_qualidade_ar}: {e}")

# Limpeza de dados (remover valores nulos)
df_emissoes = df_emissoes.dropna()
df_qualidade_ar = df_qualidade_ar.dropna()

# Definir caminhos para salvar os arquivos limpos
caminho_emissoes_limpo = "C:/Users/Andreia/Ambiente de Trabalho/Andreia/AndreiaEIC/1º Simestre/CD-2025/Trabalho/TrabalhoBigData/datasets/emissoes_limpo.csv"
caminho_qualidade_ar_limpo = "C:/Users/Andreia/Ambiente de Trabalho/Andreia/AndreiaEIC/1º Simestre/CD-2025/Trabalho/TrabalhoBigData/datasets/qualidade_ar_limpo.csv"

# Salvar os dados limpos
df_emissoes.to_csv(caminho_emissoes_limpo, index=False)
df_qualidade_ar.to_csv(caminho_qualidade_ar_limpo, index=False)

# Verificar se os arquivos foram realmente criados
print("\n📂 Arquivos gerados:")
print(os.listdir("C:/Users/Andreia/Ambiente de Trabalho/Andreia/AndreiaEIC/1º Simestre/CD-2025/Trabalho/TrabalhoBigData/datasets/"))

print("\n✅ Processamento finalizado! Dados limpos salvos.")
