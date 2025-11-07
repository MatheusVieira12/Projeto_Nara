# import pandas as pd
# import matplotlib.pyplot as plt

# # Carregar os dados
# clientes = pd.read_csv("NARA_csv/clientes.csv")
# produtos = pd.read_csv("NARA_csv/produtos_final.csv")
# vendas = pd.read_csv("NARA_csv/vendas_csv/vendas_concatenadas.csv")
# avaliacoes = pd.read_csv("NARA_csv/avaliacoes.csv")
# atendimentos = pd.read_csv("NARA_csv/atendimentos_convertido.csv")

# # Merge com produtos (para adicionar Preco)
# df = pd.merge(vendas, produtos[['ID_Produto', 'Preco']], on='ID_Produto', how='left')

# # Merge com avaliações (Nota por produto)
# df = pd.merge(df, avaliacoes[['ID_Produto', 'Nota']], on='ID_Produto', how='left')

# # Merge com atendimentos (Tempo de Resposta por cliente)
# df = pd.merge(df, atendimentos[['ID_Cliente', 'Tempo_Resposta']], on='ID_Cliente', how='left')

# # Matriz de correlação
# correlacoes = df[['Preco', 'Nota', 'Tempo_Resposta', 'Valor_Total']].corr()
# print("Matriz de Correlação:\n", correlacoes)

# # Gráficos
# plt.figure(figsize=(10,6))
# plt.scatter(df['Preco'], df['Nota'], alpha=0.6)
# plt.title('Preço vs Nota')
# plt.xlabel('Preço')
# plt.ylabel('Nota')
# plt.grid(True)
# plt.show()

# plt.figure(figsize=(10,6))
# plt.scatter(df['Preco'], df['Tempo_Resposta'], alpha=0.6)
# plt.title('Preço vs Tempo de Resposta')
# plt.xlabel('Preço')
# plt.ylabel('Tempo de Resposta')
# plt.grid(True)
# plt.show()

# plt.figure(figsize=(10,6))
# plt.scatter(df['Preco'], df['Valor_Total'], alpha=0.6)
# plt.title('Preço vs Valor de Venda')
# plt.xlabel('Preço')
# plt.ylabel('Valor de Venda')
# plt.grid(True)
# plt.show()

# plt.figure(figsize=(10,6))
# plt.scatter(df['Nota'], df['Tempo_Resposta'], alpha=0.6)
# plt.title('Nota vs Tempo de Resposta')
# plt.xlabel('Nota')
# plt.ylabel('Tempo de Resposta')
# plt.grid(True)
# plt.show()

# plt.figure(figsize=(10,6))
# plt.scatter(df['Nota'], df['Valor_Total'], alpha=0.6)
# plt.title('Nota vs Valor de Venda')
# plt.xlabel('Nota')
# plt.ylabel('Valor de Venda')
# plt.grid(True)
# plt.show()



import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
clientes = pd.read_csv("NARA_csv/clientes.csv")
produtos = pd.read_csv("NARA_csv/produtos_final.csv")
vendas = pd.read_csv("NARA_csv/vendas_concatenadas_limpa.csv")
avaliacoes = pd.read_csv("NARA_csv/avaliacoes.csv")
atendimentos = pd.read_csv("NARA_csv/atendimentos_convertido.csv")

# Mesclar os dados necessários
df = pd.merge(vendas, produtos[['ID_Produto', 'Preco']], on='ID_Produto', how='left')
df = pd.merge(df, avaliacoes[['ID_Produto', 'Nota']], on='ID_Produto', how='left')
df = pd.merge(df, atendimentos[['ID_Cliente', 'Tempo_Resposta']], on='ID_Cliente', how='left')

# Calcular matriz de correlação
correlacoes = df[['Preco', 'Nota', 'Tempo_Resposta', 'Valor_Total']].corr()
print("Matriz de Correlação:\n", correlacoes)

# Criar subplots manualmente
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle("Gráficos de Dispersão das Correlações", fontsize=16)

# Preco x Nota
axes[0, 0].scatter(df['Preco'], df['Nota'], alpha=0.6)
axes[0, 0].set_title('Preco x Nota')
axes[0, 0].grid(True)

# Preco x Tempo_Resposta
axes[0, 1].scatter(df['Preco'], df['Tempo_Resposta'], alpha=0.6, color='orange')
axes[0, 1].set_title('Preco x Tempo de Resposta')
axes[0, 1].grid(True)

# Preco x Valor_Total
axes[0, 2].scatter(df['Preco'], df['Valor_Total'], alpha=0.6, color='green')
axes[0, 2].set_title('Preco x Valor de Venda')
axes[0, 2].grid(True)

# Nota x Tempo_Resposta
axes[1, 0].scatter(df['Nota'], df['Tempo_Resposta'], alpha=0.6, color='red')
axes[1, 0].set_title('Nota x Tempo de Resposta')
axes[1, 0].grid(True)

# Nota x Valor_Total
axes[1, 1].scatter(df['Nota'], df['Valor_Total'], alpha=0.6, color='purple')
axes[1, 1].set_title('Nota x Valor de Venda')
axes[1, 1].grid(True)

# Tempo_Resposta x Valor_Total
axes[1, 2].scatter(df['Tempo_Resposta'], df['Valor_Total'], alpha=0.6, color='brown')
axes[1, 2].set_title('Tempo de Resposta x Valor de Venda')
axes[1, 2].grid(True)

# Ajustar layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()




