import pandas as pd


vendas = pd.read_csv("vendas.csv", parse_dates=["Data"])
campanhas = pd.read_csv("campanhas_corrigido.csv", parse_dates=["Data_Inicio", "Data_Fim"])

vendas["Canal"] = vendas["Canal"].str.lower().str.strip()
campanhas["Canal"] = campanhas["Canal"].str.lower().str.strip()

resultados = []

for _, row in campanhas.iterrows():
    vendas_campanha = vendas[
        (vendas["Canal"] == row["Canal"]) &
        (vendas["Data"] >= row["Data_Inicio"]) &
        (vendas["Data"] <= row["Data_Fim"])
    ]
    total_vendas = vendas_campanha["Valor_Total"].sum()
    if row["Custo"] > 0:
        roi = total_vendas / row["Custo"]
    else:
        roi = 0
    resultados.append({
        "ID_Campanha": row["ID_Campanha"],
        "Tipo_Campanha": row["Tipo_Campanha"],
        "Canal": row["Canal"],
        "Vendas_Totais": total_vendas,
        "Custo": row["Custo"],
        "ROI": roi,
        "Retorno_%": (roi - 1) * 100
    })


impacto = pd.DataFrame(resultados)

print(impacto.sort_values("ROI", ascending=False))
campanhas.to_csv('roi.csv',sep =',', index= False)

import matplotlib.pyplot as plt







impacto_filtrado = impacto[impacto['Vendas_Totais'] > 0]

 #BOXPLOT 1: Vendas Totais#
plt.figure(figsize=(8,5))
plt.boxplot(impacto_filtrado['Vendas_Totais'], showmeans=True, meanline=True,
            boxprops=dict(color='blue'),
            meanprops=dict(color='red', linewidth=2),
            medianprops=dict(color='green', linewidth=2))
plt.title('Dispersão das Vendas Totais das Campanhas')
plt.ylabel('Vendas Totais (R$)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

#  BOXPLOT 2: Custos 
plt.figure(figsize=(8,5))
plt.boxplot(impacto_filtrado['Custo'], showmeans=True, meanline=True,
            boxprops=dict(color='blue'),
            meanprops=dict(color='red', linewidth=2),
            medianprops=dict(color='green', linewidth=2))
plt.title('Dispersão dos Custos das Campanhas')
plt.ylabel('Custo (R$)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

#  BOXPLOT 3: ROI
plt.figure(figsize=(8,5))
plt.boxplot(impacto_filtrado['ROI'], showmeans=True, meanline=True,
            boxprops=dict(color='blue'),
            meanprops=dict(color='red', linewidth=2),
            medianprops=dict(color='green', linewidth=2))
plt.title('Dispersão do ROI das Campanhas')
plt.ylabel('ROI')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


# DISPERSÃO 1: Custo x Vendas Totais 
plt.figure(figsize=(6,5))
plt.scatter(impacto_filtrado['Custo'], impacto_filtrado['Vendas_Totais'], alpha=0.7, color='royalblue')
plt.axhline(impacto_filtrado['Vendas_Totais'].mean(), color='red', linestyle='--', label='Média Vendas')
plt.axvline(impacto_filtrado['Custo'].mean(), color='green', linestyle='--', label='Média Custo')
plt.title('Correlação: Custo x Vendas Totais')
plt.xlabel('Custo (R$)')
plt.ylabel('Vendas Totais (R$)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# DISPERSÃO 2: Custo x ROI
plt.figure(figsize=(6,5))
plt.scatter(impacto_filtrado['Custo'], impacto_filtrado['ROI'], alpha=0.7, color='orange')
plt.axhline(impacto_filtrado['ROI'].mean(), color='red', linestyle='--', label='Média ROI')
plt.axvline(impacto_filtrado['Custo'].mean(), color='green', linestyle='--', label='Média Custo')
plt.title('Correlação: Custo x ROI')
plt.xlabel('Custo (R$)')
plt.ylabel('ROI')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
