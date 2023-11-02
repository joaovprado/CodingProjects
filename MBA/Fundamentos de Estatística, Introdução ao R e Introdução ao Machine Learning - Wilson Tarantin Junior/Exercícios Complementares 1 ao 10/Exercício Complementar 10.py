from scipy.stats import *
import numpy as np


alpha = 0.05 #Significância

media_esperada = 60
n_obs = 36
media = 65
desv = 3.5


t_value_crit = t.isf(alpha, n_obs-1)

print(t_value_crit)
print(f'H1 (hipótese nula rejeitada), pois o valor-F ({alpha:.2f}) é maior do que o valor-F crítico definido de {alpha:.2f}' if alpha > alpha else f'H0 (hipótese nula aceita), pois o valor-F ({alpha:.2f}) é menor do que o valor-F crítico definido de {alpha:.2f}')
print('Ou seja, os tempos de espera de cada hospital observado são parecidos, pois as variâncias são parecidas, então não há diferença entre os hospitais.')