import pandas as pd

# Lê o arquivo dentro da pasta NARA_csv
df = pd.read_csv("NARA_csv/venda 1.csv")

# Remove a parte da hora
df['Data'] = pd.to_datetime(df['Data']).dt.date

# Salva o novo arquivo na mesma pasta
df.to_csv("NARA_csv/vendas_1_semH.csv", index=False)

print("✅ Novo arquivo criado em 'NARA_csv/vendass_1_semH.csv'")
