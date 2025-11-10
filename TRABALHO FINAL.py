import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar os dados
vendas1 = pd.read_csv('vendas.csv')
vendas2 = pd.read_csv('venda_1.csv')
vendas3 = pd.read_csv('venda_2.csv')
vendas4 = pd.read_csv('venda_3.csv')
produtos = pd.read_csv('produto.csv')
avaliacoes = pd.read_csv('avaliacoes.csv')
atendimentos = pd.read_csv('atendimentos.csv')
campanhas = pd.read_csv('campanhas_corrigido.csv')
clientes = pd.read_csv('clientes.csv')
sem_marca = pd.read_csv('produtos_sem_marca_corrigidos.csv')
novo_produto = pd.read_csv('Produto adicional.csv', sep=';', )
produtos_completo = pd.concat([produtos, novo_produto], ignore_index=True)
produtos_completo.drop_duplicates(subset='Nome_Produto', inplace=True)
produtos_completo

# Criação do DataFrame final

vendas_novos = pd.concat([vendas2, vendas3, vendas4], ignore_index=True)

vendas_novos["Valor_Total"] = vendas_novos["Valor_Total"].astype(str).str[:-2] + "." + vendas_novos["Valor_Total"].astype(str).str[-2:]

# Convertendo de volta para número (float)
vendas_novos["Valor_Total"] = vendas_novos["Valor_Total"].astype(float)

#removendo possiveis ID_venda duplicados
vendas_novos = vendas_novos.drop_duplicates(subset='ID_Venda')




vendas_novos['Data'] = vendas_novos['Data'].astype(str).str.replace(' 00:00:00', '', regex=False)
vendas = pd.concat([vendas1, vendas_novos], ignore_index=True)
produtos_completo.set_index('ID_Produto', inplace=True)
sem_marca.set_index('ID_Produto', inplace=True)
tabela_join = produtos_completo.join(sem_marca, how='left', rsuffix='_corrigido')
tabela_join['Marca'] = tabela_join['Marca'].fillna(tabela_join['Marca_corrigido'])
tabela_join.drop(columns=['Marca_corrigido'], inplace=True)
produtos_completo = tabela_join.reset_index()
produtos_completo
df = vendas.merge(clientes, on='ID_Cliente', how='left').merge(produtos_completo, on='ID_Produto', how='left')

# Criação da coluna faixa_etaria
df["faixa_etaria"] = "Adulto"      
df.loc[df["Idade"] < 23, "faixa_etaria"] = "Jovem"
df.loc[df["Idade"] > 65, "faixa_etaria"] = "Idoso"


# groupyby faixa etaria e percentual de compras

compra_por_faixa = df.groupby("faixa_etaria")["Valor_Total"].sum().reset_index()
total = compra_por_faixa["Valor_Total"].sum()
compra_por_faixa["percentual"] = (compra_por_faixa["Valor_Total"] / total * 100).round(2)
#print(compra_por_faixa) 

# groupyby faixa etaria, canal de compra e percentual de compras

compra_por_faixa_canal = df.groupby(["faixa_etaria", "Canal"])["Valor_Total"].sum().reset_index()
total_canal = compra_por_faixa_canal["Valor_Total"].sum()
compra_por_faixa_canal["percentual"] = (compra_por_faixa_canal["Valor_Total"] / total_canal * 100).round(2)
print(compra_por_faixa_canal)


# groupyby produto mais vendido por faixa etaria
produto_mais_vendido = df.groupby(["faixa_etaria", "Nome_Produto"])["Valor_Total"].sum().reset_index()
produto_mais_vendido = produto_mais_vendido.loc[produto_mais_vendido.groupby("faixa_etaria")["Valor_Total"].idxmax()]
print(produto_mais_vendido)

#groupyby venda de produto por percentual valor total
venda_produto = df.groupby("Nome_Produto")["Valor_Total"].sum().reset_index()
total_produto = venda_produto["Valor_Total"].sum()
venda_produto["percentual"] = (venda_produto["Valor_Total"] / total_produto * 100).round(2)
print(venda_produto.sort_values(by="percentual", ascending=False))

# identificação dos outliers abaixo do limite inferior e acima do limite superior
venda_array = np.array(venda_produto['percentual'])

q1 = np.percentile(venda_array, 25)
q3 = np.percentile(venda_array, 75)
media = np.mean(venda_array)
mediana = np.median(venda_array)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
outliers_inferior = venda_produto[venda_produto['percentual'] < q1]
outliers_superior = venda_produto[venda_produto['percentual'] > limite_superior]
print(outliers_inferior)


# groupyby faixa etaria, sexo e percentual de compras

compra_por_faixa_sexo = df.groupby(["faixa_etaria", "Sexo"])["Valor_Total"].sum().reset_index()
total_sexo = compra_por_faixa_sexo["Valor_Total"].sum()
compra_por_faixa_sexo["percentual"] = (compra_por_faixa_sexo["Valor_Total"] / total_sexo * 100).round(2)
print(compra_por_faixa_sexo)




# grafico de dispersao faixa etaria vs valor total
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df["faixa_etaria"], df["Valor_Total"])
ax.set_title('Gráfico de Dispersão - Faixa Etária vs Valor Total das Compras')
ax.set_xlabel('Faixa Etária')
ax.set_ylabel('Valor Total (R$)')
plt.show()



# grafico de dispersao sexo vs valor total
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df["Sexo"], df["Valor_Total"])
ax.set_title('Gráfico de Dispersão - Sexo vs Valor Total das Compras')
ax.set_xlabel('Sexo')
ax.set_ylabel('Valor Total (R$)')
plt.show()

# grafico de dispersao canal vs valor total
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df["Canal"], df["Valor_Total"])
ax.set_title('Gráfico de Dispersão - Canal vs Valor Total das Compras')
ax.set_xlabel('Canal')
ax.set_ylabel('Valor Total (R$)')
plt.show()

# quadro boxplot todos os boxplots juntos com showmens

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
df.boxplot(column='Valor_Total', by='faixa_etaria', ax=axs[0, 0])
axs[0, 0].set_title('Boxplot - Valor Total das Compras por Faixa Etária')
axs[0, 0].set_xlabel('Faixa Etária')
axs[0, 0].set_ylabel('Valor Total (R$)')
df.boxplot(column='Valor_Total', by='Sexo', ax=axs[0, 1])
axs[0, 1].set_title('Boxplot - Valor Total das Compras por Sexo')
axs[0, 1].set_xlabel('Sexo')
axs[0, 1].set_ylabel('Valor Total (R$)')
df.boxplot(column='Valor_Total', by='Categoria', ax=axs[1, 0])
axs[1, 0].set_title('Boxplot - Valor Total das Compras por Categoria')
axs[1, 0].set_xlabel('Categoria')
axs[1, 0].set_ylabel('Valor Total (R$)')
axs[1, 1].axis('off')  # Desativa o quarto subplot vazio
axs[1, 1].text(0.5, 0.7, 'Boxplot relação Faixa Etária e Valor Total', horizontalalignment='center', verticalalignment='center', fontsize=10, color='black', transform=axs[1, 1].transAxes)
axs[1, 1].text(0.5, 0.5, 'Boxplot relação Sexo e Valor Total', horizontalalignment='center', verticalalignment='center', fontsize=10, color='black', transform=axs[1, 1].transAxes)
axs[1, 1].text(0.5, 0.3, 'Boxplot relação Categoria e Valor Total', horizontalalignment='center', verticalalignment='center', fontsize=10, color='black', transform=axs[1, 1].transAxes)
plt.suptitle('Análise de Valor Total das Compras')
plt.tight_layout()
plt.show()
