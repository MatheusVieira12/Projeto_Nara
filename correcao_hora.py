import pandas as pd

df = pd.read_csv("NARA_csv/venda 3.csv")

# Remove a parte da hora
df['Data'] = pd.to_datetime(df['Data']).dt.date

# Salva o novo arquivo na mesma pasta
df.to_csv("NARA_csv/venda_3_semH.csv", index=False)

print("✅ Novo arquivo criado em 'NARA_csv/venda_3_semH.csv'")
