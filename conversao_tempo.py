import pandas as pd

df = pd.read_csv("NARA_csv/atendimentos.csv")

# Converter para minutos
df["Tempo_Resposta"] = df["Tempo_Resposta"] * 60

df.to_csv("NARA_csv/atendimentos_convertidossss.csv", index=False) 
