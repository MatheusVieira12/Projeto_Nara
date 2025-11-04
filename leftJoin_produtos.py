import pandas as pd

# Ler os arquivos diretamente com o caminho completo
produtos = pd.read_csv("NARA_csv/produtos.csv", sep=",")
corrigidos = pd.read_csv("NARA_csv/produtos_sem_marca_corrigidos.csv", sep=",")

# Realizar a concatenação com merge
df = produtos.merge(corrigidos[["ID_Produto", "Marca"]], on="ID_Produto",
    how="left",
    suffixes=("", "_corrigida")
)

# Preencher valores ausentes na coluna 'Marca' com os valores corrigidos
df["Marca"] = df["Marca"].fillna(df["Marca_corrigida"])

# Remover a coluna auxiliar 'Marca_corrigida'
df = df.drop(columns=["Marca_corrigida"])

# Salvar o arquivo final com as alterações
df.to_csv("NARA_csv/produtos_atualizado.csv", index=False, encoding="utf-8")

print("✅ Arquivo 'produtos_atualizado.csv' criado com sucesso!")
