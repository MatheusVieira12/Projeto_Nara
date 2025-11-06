import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

atendimentos_df = pd.read_csv('atendimentos_novo.csv', sep = ',')


atendimentos_df['Tempo_Resp']= atendimentos_df['Tempo_Resposta']*60
atendimentos_df= atendimentos_df.drop('Tempo_Resposta', axis=1)


satisfacao_notas = atendimentos_df.groupby('Tipo')['Nota_Satisfacao'].sum().reset_index()


satisfacao_notas_array= np.array (satisfacao_notas['Nota_Satisfacao'])
q1_satisfacao_notas = np.percentile(satisfacao_notas_array, 25)
q2_satisfacao_notas= np.percentile(satisfacao_notas_array,50)
q3_satisfacao_notas = np.percentile(satisfacao_notas_array,75)
mediana_satisfacao_notas = np.median(satisfacao_notas_array)
media_satisfacao_notas = np.mean(satisfacao_notas_array)

print(f'Primeiro Quartil notas (01): {q1_satisfacao_notas}')
print(f'Segundo Quartil notas  (02): {q2_satisfacao_notas}')
print(f'Terceiro Quartil notas  (03): {q3_satisfacao_notas}')
print(f'Mediana notas : {mediana_satisfacao_notas}')
print(f'Media notas : {media_satisfacao_notas}')


iqr = q3_satisfacao_notas - q1_satisfacao_notas
limite_superior =  q3_satisfacao_notas + (1.5 * iqr)

notas_outliers= satisfacao_notas.loc[satisfacao_notas['Nota_Satisfacao'] >= limite_superior ] 
notas_outliers.sort_values(by = 'Nota_Satisfacao', ascending = False)
print(notas_outliers)


satisfacao_tempo = atendimentos_df.groupby('Tipo')['Tempo_Resp'].mean().reset_index()


satisfacao_tempo_array= np.array (satisfacao_tempo['Tempo_Resp'])
q1_satisfacao_tempo = np.percentile(satisfacao_tempo_array, 25)
q2_satisfacao_tempo= np.percentile(satisfacao_tempo_array,50)
q3_satisfacao_tempo = np.percentile(satisfacao_tempo_array,75)
mediana_satisfacao_tempo = np.median(satisfacao_tempo_array)
media_satisfacao_tempo = np.mean(satisfacao_tempo_array)

print(f'Primeiro Quartil tempo (01): {q1_satisfacao_tempo}')
print(f'Segundo Quartil tempo (02): {q2_satisfacao_tempo}')
print(f'Terceiro Quartil tempo (03): {q3_satisfacao_tempo}')
print(f'Mediana tempo: {mediana_satisfacao_tempo}')
print(f'Media tempo: {media_satisfacao_tempo}')


iqr = q3_satisfacao_tempo - q1_satisfacao_tempo
limite_superior =  q3_satisfacao_tempo + (1.5 * iqr)


satisfacao_outliers= satisfacao_tempo.loc[satisfacao_tempo['Tempo_Resp'] >= limite_superior ] 
satisfacao_outliers.sort_values(by = 'Tempo_Resp', ascending = False)
print(satisfacao_outliers)


atendimentos_df['informações importantes']= 'Médio'
atendimentos_df.loc[atendimentos_df['Tempo_Resp']> q3_satisfacao_tempo,'informações importantes']= 'Ruim'
atendimentos_df.loc[atendimentos_df['Tempo_Resp'] <q1_satisfacao_tempo,'informações importantes']= 'Bom'


atendimentos_df.to_csv('atendimentos.csv',sep =',', index= False)


avaliacao = atendimentos_df.groupby('informações importantes')['Tempo_Resp'].sum().reset_index()



# Boxplot das notas de satisfação por tipo de atendimento
plt.figure(figsize=(8,5))
atendimentos_df.boxplot(column='Nota_Satisfacao', by='Tipo', grid=False, showmeans = True)
plt.title('Dispersão das Notas de Satisfação por Tipo de Atendimento')
plt.suptitle('')  # remove o título automático extra
plt.xlabel('Tipo de Atendimento')
plt.ylabel('Nota de Satisfação')
plt.show()

# Boxplot do tempo de resposta por tipo de atendimento
plt.figure(figsize=(8,5))
atendimentos_df.boxplot(column='Tempo_Resp', by='Tipo', grid=False, showmeans = True)
plt.title('Dispersão do Tempo de Resposta por Tipo de Atendimento')
plt.suptitle('')
plt.xlabel('Tipo de Atendimento')
plt.ylabel('Tempo de Resposta (minutos)')
plt.show()


# Correlação entre Tempo de Resposta e Nota de Satisfação
plt.figure(figsize=(6,5))
plt.scatter(atendimentos_df['Tempo_Resp'], atendimentos_df['Nota_Satisfacao'], alpha=0.6)
plt.title('Correlação: Tempo de Resposta x Nota de Satisfação')
plt.xlabel('Tempo de Resposta (minutos)')
plt.ylabel('Nota de Satisfação')
plt.grid(True)
plt.show()

# Correlação entre Tempo de Resposta e Tipo de Atendimento (média por tipo)
media_por_tipo = atendimentos_df.groupby('Tipo')[['Tempo_Resp', 'Nota_Satisfacao']].mean().reset_index()

plt.figure(figsize=(6,5))
plt.scatter(media_por_tipo['Tempo_Resp'], media_por_tipo['Nota_Satisfacao'])
for i, row in media_por_tipo.iterrows():
    plt.text(row['Tempo_Resp'], row['Nota_Satisfacao'], row['Tipo'])
plt.title('Média de Nota x Tempo de Resposta por Tipo de Atendimento')
plt.xlabel('Tempo Médio de Resposta (minutos)')
plt.ylabel('Nota Média de Satisfação')
plt.grid(True)
plt.show()