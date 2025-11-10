import pandas as pd

# Carregar as bases
vendas = pd.read_csv("vendas.csv", parse_dates=["Data"])
campanhas = pd.read_csv("campanhas_corrigido.csv", parse_dates=["Data_Inicio", "Data_Fim"])


vendas["Canal"] = vendas["Canal"].str.lower().str.strip()
campanhas["Canal"] = campanhas["Canal"].str.lower().str.strip()


vendas_campanhas = vendas.merge(
    campanhas,
    on="Canal",
    how="left",
    suffixes=("_venda", "_campanha")
) 

vendas_campanhas = vendas_campanhas[
    (vendas_campanhas["Data"] >= vendas_campanhas["Data_Inicio"]) &
    (vendas_campanhas["Data"] <= vendas_campanhas["Data_Fim"])
]


impacto = vendas_campanhas.groupby(["ID_Campanha", "Tipo_Campanha", "Canal"], as_index=False).agg({
    "Valor_Total": "sum",
    "Custo": "mean"
})

impacto["ROI"] = impacto["Valor_Total"] / impacto["Custo"]
impacto["Retorno_%"] = (impacto["ROI"] - 1) * 100

print(impacto.sort_values("ROI", ascending=False))

