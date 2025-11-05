import pandas as pd

# Carregar os arquivos CSV
df1 = pd.read_csv("NARA_csv/vendas_csv/vendas.csv")
df2 = pd.read_csv("NARA_csv/vendas_csv/venda_1_semH.csv")
df3 = pd.read_csv("NARA_csv/vendas_csv/vendas_2_semH.csv")
df4 = pd.read_csv("NARA_csv/vendas_csv/venda_3_semH.csv")

# Concatenar
df_vendas = pd.concat([df1, df2, df3, df4], ignore_index=True)


print(df_vendas.head())

# Salvar o CSV final
df_vendas.to_csv("NARA_csv/vendas_csv/vendas_concatenadas.csv", index=False)
