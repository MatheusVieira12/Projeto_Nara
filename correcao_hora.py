import pandas as pd

path = r"C:\Users\PC\Desktop\projetos\Projeto_Nara\NARA_csv"

df = pd.read_csv(fr"{path}\venda 1.csv")

# Converte a coluna data para datetime e remove a parte da hora
df['Data'] = pd.to_datetime(df['Data']).dt.date

novo_arquivo = fr"{path}\venda_1_semH.csv"
df.to_csv(novo_arquivo, index=False)

print(f"✅ Novo arquivo criado com sucesso: {novo_arquivo}")
