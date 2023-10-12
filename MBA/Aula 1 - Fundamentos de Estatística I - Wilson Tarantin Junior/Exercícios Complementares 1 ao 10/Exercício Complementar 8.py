from scipy.stats import f, levene
import numpy as np
import pandas as pd

df = pd.read_excel('C:/Users/jvict/OneDrive/Documentos/CodingProjects/Aula 1 - Fundamentos de Estatística I - Wilson Tarantin Junior/Lista de Exercícios - Complementares.xlsx', sheet_name='Exercício 8', usecols='A,B', nrows = 18, header = 0)

alpha = 0.05 #Significância

group1 = df['Local A (mm)']
group2 = df['Local B (mm)']
df1 =  len(group1) - 1
df2 =  len(group2) - 1


# Calculate the F-statistic
f_value = np.var(group1) / np.var(group2)
f_value_crit = f.isf(alpha, df1, df2)

print(f'H1 (hipótese nula rejeitada), pois o valor-F ({f_value:.2f}) é maior do que o valor-F crítico definido de {f_value_crit:.2f}' if f_value > f_value_crit else f'H0 (hipótese nula aceita), pois o valor-F ({f_value:.2f}) é menor do que o valor-F crítico definido de {f_value:.2f}')
print('Ou seja, as distribuições observadas são muito diferentes, pois as variâncias são diferentes, então há diferença entre os locais.')