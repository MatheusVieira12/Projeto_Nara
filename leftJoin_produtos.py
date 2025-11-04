import pandas as pd

# Caminho da pasta
path = r"C:\Users\PC\Desktop\projetos\Projeto_Nara\NARA_csv"

# Ler os arquivos
produtos = pd.read_csv(fr"{path}\produtos.csv")
corrigidos = pd.read_csv(fr"{path}\produtos_sem_marca_corrigidos.csv")


df = produtos.merge(
    corrigidos[["ID_Produto", "Marca"]],
    on="ID_Produto",
    how="left",
    suffixes=("", "_corrigida")
)

# Preencher valores ausentes em 'Marca' com a 'Marca_corrigida'
df["Marca"] = df["Marca"].fillna(df["Marca_corrigida"])

# Remover a coluna auxiliar
df = df.drop(columns=["Marca_corrigida"])

# Salvar o resultado
df.to_csv(fr"{path}\produtos_atualizado.csv", index=False, encoding="utf-8")

print("✅ Arquivo 'produtos_atualizado.csv' criado com sucesso!")
