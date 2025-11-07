import pandas as pd


df1 = pd.read_csv("NARA_csv/vendas_csv/vendas.csv")
df2 = pd.read_csv("NARA_csv/vendas_csv/vendas_1_limpo.csv")
df3 = pd.read_csv("NARA_csv/vendas_csv/vendas_2_limpo.csv")
df4 = pd.read_csv("NARA_csv/vendas_csv/vendas_3_limpo.csv")

# Concatenar
df_vendas = pd.concat([df1, df2, df3, df4], ignore_index=True)


print(df_vendas.head())

df_vendas.to_csv("NARA_csv/vendas_concatenadas_limpa.csv", index=False)

