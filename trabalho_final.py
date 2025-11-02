import pandas as pd

# Carregar as bases
vendas = pd.read_csv("vendas.csv", parse_dates=["Data"])
campanhas = pd.read_csv("campanhas_corrigido.csv", parse_dates=["Data_Inicio", "Data_Fim"])

# Garantir que os canais tenham o mesmo formato
vendas["Canal"] = vendas["Canal"].str.lower().str.strip()
campanhas["Canal"] = campanhas["Canal"].str.lower().str.strip()

# Fazer um merge condicional (canal + intervalo de datas)
vendas_campanhas = vendas.merge(
    campanhas,
    on="Canal",
    how="left",
    suffixes=("_venda", "_campanha")
)

# Filtrar somente vendas dentro do período da campanha
vendas_campanhas = vendas_campanhas[
    (vendas_campanhas["Data"] >= vendas_campanhas["Data_Inicio"]) &
    (vendas_campanhas["Data"] <= vendas_campanhas["Data_Fim"])
]

# Agora temos as vendas associadas a campanhas
# Vamos calcular o total de vendas e o ROI
impacto = vendas_campanhas.groupby(["ID_Campanha", "Tipo_Campanha", "Canal"], as_index=False).agg({
    "Valor_Total": "sum",
    "Custo": "mean"
})

impacto["ROI"] = impacto["Valor_Total"] / impacto["Custo"]
impacto["Retorno_%"] = (impacto["ROI"] - 1) * 100

print(impacto.sort_values("ROI", ascending=False))

impacto.to_csv("impacto_campanhas.csv", index=False, encoding='utf-8')