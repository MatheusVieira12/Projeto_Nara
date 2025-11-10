import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

# 1️⃣ Carregar os dados
clientes = pd.read_csv("NARA_csv/clientes.csv")
produtos = pd.read_csv("NARA_csv/produtos_final.csv")
vendas = pd.read_csv("NARA_csv/vendas_concatenadas_limpa.csv")
avaliacoes = pd.read_csv("NARA_csv/avaliacoes.csv")
atendimentos = pd.read_csv("NARA_csv/atendimentos_convertido.csv")

# 2️⃣ Unir os dados
df = pd.merge(vendas, produtos[['ID_Produto', 'Preco']], on='ID_Produto', how='left')
df = pd.merge(df, avaliacoes[['ID_Produto', 'Nota']], on='ID_Produto', how='left')
df = pd.merge(df, atendimentos[['ID_Cliente', 'Tempo_Resposta']], on='ID_Cliente', how='left')

# 3️⃣ Garantir tipos numéricos
df[['Valor_Total', 'Preco', 'Nota', 'Tempo_Resposta', 'Quantidade']] = df[['Valor_Total', 'Preco', 'Nota', 'Tempo_Resposta', 'Quantidade']].apply(pd.to_numeric, errors='coerce')

# 4️⃣ Matriz de correlação
correlacoes = df[['Preco', 'Nota', 'Tempo_Resposta', 'Valor_Total', 'Quantidade']].corr()
print("📊 Matriz de Correlação:\n", correlacoes, "\n")

# 5️⃣ Correlações fortes
print("🔥 Correlações fortes (>|0.5|):\n")
print(correlacoes[(correlacoes.abs() > 0.5) & (correlacoes.abs() < 1.0)], "\n")

# 6️⃣ Gráficos em subplot
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# --- Gráfico 1: Quantidade x Valor_Total ---
ax1 = axes[0]
ax1.scatter(df['Quantidade'], df['Valor_Total'], alpha=0.6, color='teal')
ax1.set_title('Quantidade x Valor_Total')
ax1.set_xlabel('Quantidade')
ax1.set_ylabel('Valor_Total')

# --- Gráfico 2: Preço x Valor_Total ---
ax2 = axes[1]
ax2.scatter(df['Preco'], df['Valor_Total'], alpha=0.6, color='green')
ax2.set_title('Preço x Valor_Total')
ax2.set_xlabel('Preço')
ax2.set_ylabel('Valor_Total')

# Ajuste final do layout
plt.tight_layout()
plt.show()



