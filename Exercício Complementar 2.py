from scipy.stats import variation
import pandas as pd

df = pd.read_excel('C:/Users/jvict/OneDrive/Documentos/CodingProjects/Aula 1 - Fundamentos de Estatística I - Wilson Tarantin Junior/Lista de Exercícios - Complementares.xlsx', sheet_name='Exercício 2', usecols='B,C', header = 0)
    
describe = df.describe().rename({'count': 'Nº de Observações', 'mean' : 'Média', 'std': 'Desvio Padrão', 'min': 'Mínimo', '25%': '1º Quartil', '50%': 'Mediana', '75%': '3º Quartil', 'max': 'Máximo'})

#moda = df.mode() # Nn tem moda, então o retorno é uma outra tabela

percentil = df.quantile([.8, .9, .27, .64]).rename({.8: '8º Decil', .9: '9º Decil', .27: '27º Percentil', .64 : '64º Percentil'})

amplitude = (df.max() - df.min()).to_frame().transpose().rename({0: 'Amplitude'})

variancia = df.var().to_frame().transpose().rename({0: 'Variância'})

erroPadrao = df.sem().to_frame().transpose().rename({0: 'Erro Padrão'})

coef_variacao = pd.DataFrame(variation(df, nan_policy='omit')*100).transpose().rename(index = {0: 'Coeficiente de variação'}, columns = {0: 'Ação 1', 1: 'Ação 2'}) # type: ignore

print(pd.concat([describe, percentil, amplitude, variancia, erroPadrao,coef_variacao]))

print('')
print('')

print('Não tem moda, pq os valores nn se repetem')

print('')
print('')

corr = df['Ação 1'].corr(df['Ação 2'])
print('Correlação: ', corr) 
print('Estatística T Correlação: ', corr/((1-corr**2)/(df['Ação 1'].count()-2))**.5)
print('p-Valor bicaudal: não consegui chegar')
print('Valor Crítico (5%): não consegui chegar')

print('')
print('')
