import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 


clientes = pd.read_csv("NARA_csv/clientes.csv")
produtos = pd.read_csv("NARA_csv/produtos_final.csv")
vendas = pd.read_csv("NARA_csv/vendas_concatenadas_limpa.csv")
avaliacoes = pd.read_csv("NARA_csv/avaliacoes.csv")
atendimentos = pd.read_csv("NARA_csv/atendimentos_convertido.csv")


df = pd.merge(vendas, produtos[['ID_Produto', 'Preco']], on='ID_Produto', how='left')
df = pd.merge(df, avaliacoes[['ID_Produto', 'Nota']], on='ID_Produto', how='left')
df = pd.merge(df, atendimentos[['ID_Cliente', 'Tempo_Resposta']], on='ID_Cliente', how='left')


df[['Valor_Total', 'Preco', 'Nota', 'Tempo_Resposta', 'Quantidade']] = df[
    ['Valor_Total', 'Preco', 'Nota', 'Tempo_Resposta', 'Quantidade']
].apply(pd.to_numeric, errors='coerce')

correlacoes = df[['Preco', 'Nota', 'Tempo_Resposta', 'Valor_Total', 'Quantidade']].corr()
print("📊 Matriz de Correlação:\n", correlacoes, "\n")

print("🔥 Correlações fortes (>|0.5|):\n")
print(correlacoes[(correlacoes.abs() > 0.5) & (correlacoes.abs() < 1.0)], "\n")


fig, axes = plt.subplots(1, 3, figsize=(15, 5))


ax1 = axes[0]
ax1.scatter(df['Quantidade'], df['Valor_Total'], alpha=0.6, color='teal')
ax1.set_title('Quantidade x Valor_Total')
ax1.set_xlabel('Quantidade')
ax1.set_ylabel('Valor_Total')


ax2 = axes[1]
ax2.scatter(df['Preco'], df['Valor_Total'], alpha=0.6, color='green')
ax2.set_title('Preço x Valor_Total')
ax2.set_xlabel('Preço')
ax2.set_ylabel('Valor_Total')

ax3 = axes[2]
ax3.axis('off')
explicacao = (
    "Interpretação dos Gráficos:\n\n"
    "• O gráfico Quantidade x Valor_Total tende a mostrar uma relação positiva —\n"
    "  quanto maior a quantidade vendida, maior o valor total.\n\n"
    "• Já Preço x Valor_Total pode indicar se produtos mais caros\n"
    "  realmente geram maiores valores de venda.\n\n"
    "Essas relações ajudam a entender o comportamento das vendas\n"
    "e otimizar estratégias de precificação e estoque."
)
ax3.text(0, 0.5, explicacao, fontsize=10, va='center', ha='left', wrap=True)

plt.tight_layout()
plt.show()


