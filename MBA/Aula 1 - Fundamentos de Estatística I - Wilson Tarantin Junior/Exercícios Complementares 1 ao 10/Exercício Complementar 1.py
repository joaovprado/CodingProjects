from IPython.display import display
import pandas as pd

df = pd.read_excel('C:/Users/jvict/OneDrive/Documentos/CodingProjects/Aula 1 - Fundamentos de Estatística I - Wilson Tarantin Junior/Lista de Exercícios - Complementares.xlsx', sheet_name='Exercício 1', usecols='B', header = 0)
    
df['Renda (R$)'] = df['Renda (R$)'].apply(int)

df['Classe'] = pd.cut(df['Renda (R$)'], [0, 2000, 4000, 6000, 8000, 10000, 12000]) # Cria a cateogrização baseado nos valores dados

freq = df.Classe.value_counts().sort_index() # Frequências e ordena em ordem crescente
freq_rel = freq/sum(freq)*100 # Frequências relativas
freq_acu = freq.cumsum() # Frequências acumuladas
freq_acu_rel = freq_rel.cumsum() # Frequências acumuladas relativas

frequencias = pd.DataFrame({'Frequência': freq, 
                            'Frequência Relativa (%)': freq_rel,
                            'Frequência Acumulada': freq_acu,
                            'Frequência Acumulada Relativa (%)': freq_acu_rel})

print(frequencias)