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




fig, axes = plt.subplots(2, 3, figsize=(10, 8))

# ========= BOXPLOT 1: Vendas Totais =========
axes[0, 0].boxplot(
    impacto_filtrado['Vendas_Totais'], 
    showmeans=True, meanline=True,
    boxprops=dict(color='blue'),
    meanprops=dict(color='red', linewidth=2),
    medianprops=dict(color='green', linewidth=2)
)
axes[0, 0].set_title('Dispersão das Vendas Totais das Campanhas')
axes[0, 0].set_ylabel('Vendas Totais (R$)')
axes[0, 0].grid(True, linestyle='--', alpha=0.6)

# ========= BOXPLOT 2: Custos =========
axes[0, 1].boxplot(
    impacto_filtrado['Custo'], 
    showmeans=True, meanline=True,
    boxprops=dict(color='blue'),
    meanprops=dict(color='red', linewidth=2),
    medianprops=dict(color='green', linewidth=2)
)
axes[0, 1].set_title('Dispersão dos Custos das Campanhas')
axes[0, 1].set_ylabel('Custo (R$)')
axes[0, 1].grid(True, linestyle='--', alpha=0.6)

# ========= BOXPLOT 3: ROI =========
axes[0, 2].boxplot(
    impacto_filtrado['ROI'], 
    showmeans=True, meanline=True,
    boxprops=dict(color='blue'),
    meanprops=dict(color='red', linewidth=2),
    medianprops=dict(color='green', linewidth=2)
)
axes[0, 2].set_title('Dispersão do ROI das Campanhas')
axes[0, 2].set_ylabel('ROI')
axes[0, 2].grid(True, linestyle='--', alpha=0.6)

# ========= DISPERSÃO 1: Custo x Vendas Totais =========
axes[1, 0].scatter(impacto_filtrado['Custo'], impacto_filtrado['Vendas_Totais'], 
                   alpha=0.7, color='royalblue')
axes[1, 0].axhline(impacto_filtrado['Vendas_Totais'].mean(), color='red', linestyle='--', label='Média Vendas')
axes[1, 0].axvline(impacto_filtrado['Custo'].mean(), color='green', linestyle='--', label='Média Custo')
axes[1, 0].set_title('Correlação: Custo x Vendas Totais')
axes[1, 0].set_xlabel('Custo (R$)')
axes[1, 0].set_ylabel('Vendas Totais (R$)')
axes[1, 0].legend()
axes[1, 0].grid(True, linestyle='--', alpha=0.6)

# ========= DISPERSÃO 2: Custo x ROI =========
axes[1, 1].scatter(impacto_filtrado['Custo'], impacto_filtrado['ROI'], 
                   alpha=0.7, color='orange')
axes[1, 1].axhline(impacto_filtrado['ROI'].mean(), color='red', linestyle='--', label='Média ROI')
axes[1, 1].axvline(impacto_filtrado['Custo'].mean(), color='green', linestyle='--', label='Média Custo')
axes[1, 1].set_title('Correlação: Custo x ROI')
axes[1, 1].set_xlabel('Custo (R$)')
axes[1, 1].set_ylabel('ROI')
axes[1, 1].legend()
axes[1, 1].grid(True, linestyle='--', alpha=0.6)


axes[1, 2].axis('off')  

# Ajuste do layout
plt.tight_layout()
plt.show()