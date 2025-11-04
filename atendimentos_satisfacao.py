import pandas as pd
import numpy as np

atendimentos_df = pd.read_csv('atendimentos_novo.csv', sep = ',')


atendimentos_df['Tempo_Resp']= atendimentos_df['Tempo_Resposta']*60
atendimentos_df= atendimentos_df.drop('Tempo_Resposta', axis=1)


satisfacao_notas = atendimentos_df.groupby('Tipo')['Nota_Satisfacao'].sum().reset_index()
print(satisfacao_notas)






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





satisfacao_tempo = atendimentos_df.groupby('Tipo')['Tempo_Resp'].mean().reset_index()
print(satisfacao_tempo)

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






atendimentos_df['informações importantes']= 'Médio'
atendimentos_df.loc[atendimentos_df['Tempo_Resp']> q3_satisfacao_tempo,'informações importantes']= 'Ruim'
atendimentos_df.loc[atendimentos_df['Tempo_Resp'] <q1_satisfacao_tempo,'informações importantes']= 'Bom'

print(atendimentos_df)
atendimentos_df.to_csv('atendimentos.csv',sep =',', index= False)


avaliacao = atendimentos_df.groupby('informações importantes')['Tempo_Resp'].sum().reset_index()

print(avaliacao)
