import pandas as pd

vendas = pd.read_csv('vendas.csv')
print(vendas)

vendas1 = pd.read_csv('venda_1.csv')
print(vendas1)  

vendas2 = pd.read_csv('venda_2.csv')
print(vendas2)

vendas3 = pd.read_csv('venda_3.csv')
print(vendas3)

vendas_total = pd.concat([vendas, vendas1, vendas2, vendas3])
print(vendas_total)

clientes = pd.read_csv('clientes.csv')
print(clientes)
vendas_total_clientes = pd.merge(vendas_total, clientes, on='ID_Cliente', how='left')
print(vendas_total_clientes)

produtos = pd.read_csv('produto.csv')
print(produtos)
vendas_total_clientes_produtos = pd.merge(vendas_total_clientes, produtos, on='ID_Produto', how='left')
print(vendas_total_clientes_produtos)

vendas_total_clientes_produtos.to_csv('vendas_total_clientes_produtos.csv', index=False)