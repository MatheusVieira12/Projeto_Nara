import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


atendimentos = pd.read_csv("atendimentos.csv")
avaliacoes = pd.read_csv("avaliacoes.csv")
campanhas = pd.read_csv("campanhas_corrigido.csv")
produtos = pd.read_csv("produto.csv")
tabela_final = pd.read_csv("tabela_final.csv")
vendas = pd.read_csv('vendas.csv')
clientes = pd.read_csv('clientes.csv')  
produtos_extra = pd.read_csv('Produto adicional.csv', sep=',')

atendimentos.drop_duplicates(inplace=True)
avaliacoes.drop_duplicates(inplace=True)
campanhas.drop_duplicates(inplace=True)
produtos.drop_duplicates(inplace=True)
tabela_final.drop_duplicates(inplace=True)

vendas1 = pd.read_csv('venda_1.csv')
vendas2 = pd.read_csv('venda_2.csv' )
vendas3 = pd.read_csv('venda_3.csv' )
df_vendas = pd.concat([vendas, vendas1, vendas2, vendas3], ignore_index=True)

clientes_vendas = pd.merge(df_vendas, clientes, on="ID_Cliente", how="left")
tabela_final = pd.merge(clientes_vendas, produtos, on="ID_Produto", how="left")


tabela_final['Data'] = tabela_final['Data'].astype(str).str.replace(' 00:00:00', '', regex=False)

produtos_completo = pd.concat([produtos, produtos_extra], axis=1)




contagem = tabela_final['Nome_Produto'].value_counts().reset_index()
contagem.sort_values('count', inplace=True)

count_array = np.array(contagem['count'])

q1 = np.percentile(count_array, 25)
q3 = np.percentile(count_array, 75)
media = np.mean(count_array)
mediana = np.median(count_array)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
outliers_inferior = contagem[contagem['count'] < q1]
outliers_superior = contagem[contagem['count'] > q3]


produtos_venda = tabela_final.groupby("Nome_Produto")["Valor_Total"].sum().reset_index()
media_vendas = produtos_venda["Valor_Total"].mean()
abaixo_media = produtos_venda[produtos_venda["Valor_Total"] < media_vendas]
abaixo_media.sort_values("Valor_Total", inplace=True)


tabela_final["valor_total"] = tabela_final["Quantidade"] * tabela_final["Preco"]


tabela_final["faixa_etaria"] = "Adulto"      
tabela_final.loc[tabela_final["Idade"] < 23, "faixa_etaria"] = "Jovem"
tabela_final.loc[tabela_final["Idade"] > 65, "faixa_etaria"] = "Idoso"

perfil = tabela_final.groupby("faixa_etaria")["valor_total"].sum().reset_index()

total = perfil["valor_total"].sum()
perfil["percentual"] = (perfil["valor_total"] / total * 100).round(2)

print(perfil)
print(produtos_completo)
plt.pie(
    perfil["valor_total"],
    labels=perfil["faixa_etaria"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Participação no valor total de compras por faixa etária")
plt.show()


perfil_sexo = tabela_final.groupby("Sexo")["valor_total"].sum().reset_index()
total = perfil_sexo["valor_total"].sum()
perfil_sexo["percentual"] = (perfil_sexo["valor_total"] / total * 100).round(2)

plt.pie(
    perfil_sexo["valor_total"],
    labels=perfil_sexo["Sexo"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Participação no valor total de compras por Sexo")
plt.show()

perfil_canal = tabela_final.groupby("Canal_Aquisicao")["valor_total"].sum().reset_index()
total = perfil_canal["valor_total"].sum()
perfil_canal["percentual"] = (perfil_canal["valor_total"] / total * 100).round(2)

plt.pie(
    perfil_canal["valor_total"],
    labels=perfil_canal["Canal_Aquisicao"],
    autopct="%1.1f%%",
    startangle=90
)


plt.title("Participação no valor total por Canal de Aquisição")
plt.show()


perfil_cidade = tabela_final.groupby("Cidade")["valor_total"].sum().reset_index()
total = perfil_cidade["valor_total"].sum()
perfil_cidade["percentual"] = (perfil_cidade["valor_total"] / total * 100).round(2)


plt.bar(perfil_cidade["Cidade"], perfil_cidade["valor_total"])
plt.xticks(rotation=90)
plt.title("Valor total de compras por Cidade")
plt.ylabel("Valor total")
plt.show()


perfil_estado = tabela_final.groupby("Estado")["valor_total"].sum().reset_index()
total = perfil_estado["valor_total"].sum()
perfil_estado["percentual"] = (perfil_estado["valor_total"] / total * 100).round(2)


plt.bar(perfil_estado["Estado"], perfil_estado["valor_total"])
plt.title("Valor total de compras por Estado")
plt.ylabel("Valor total")
plt.show()


fig, axs = plt.subplots(2, 2, figsize=(12, 8))



axs[0, 0].pie(
    perfil_sexo["valor_total"],
    labels=perfil_sexo["Sexo"],
    autopct="%1.1f%%",
    startangle=90
)
axs[0, 0].set_title("Perfil de Compra por Sexo")

# --- Gráfico 2: Canal de Aquisição (Pizza)
axs[0, 1].pie(
    perfil_canal["valor_total"],
    labels=perfil_canal["Canal_Aquisicao"],
    autopct="%1.1f%%",
    startangle=90
)
axs[0, 1].set_title("Perfil por Canal de Aquisição")

# --- Gráfico 3: Cidades (Barra - 10 principais)
top_cidades = perfil_cidade.sort_values("valor_total", ascending=False).head(10)
axs[1, 0].bar(top_cidades["Cidade"], top_cidades["valor_total"])
axs[1, 0].set_title(" Cidades - Valor Total de Compras")
axs[1, 0].tick_params(axis="x", rotation=90)

# --- Gráfico 4: Estado (Barra)
axs[1, 1].pie(
    perfil["valor_total"],
    labels=perfil["faixa_etaria"],
    autopct="%1.1f%%",
    startangle=90
)
# Ajustar layout
plt.tight_layout()
plt.show()
plt.savefig("relatorio_perfis.jpeg")

plt.scatter(tabela_final['faixa_etaria'], tabela_final['Valor_Total'])
plt.title('Relação entre Faixa Etária e Valor Total das Compras')
plt.xlabel('faixa_etaria')
plt.ylabel('Valor Total das Compras')   
plt.show()

fig, ax = plt.subplots()
ax.boxplot(tabela_final['Valor_Total'], vert=True, patch_artist=True)
ax.set_title('Box Plot Example')
ax.set_ylabel('Valor_Total')
ax.set_xticklabels(['faixa_etaria'])
plt.show()

print(produtos_completo)