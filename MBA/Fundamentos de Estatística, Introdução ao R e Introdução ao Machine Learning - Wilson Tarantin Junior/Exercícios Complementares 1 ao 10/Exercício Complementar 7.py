from scipy.stats import chisquare
import numpy as np

alpha = 0.05 #Significância

# Frequências:
livroA = 29	
livroB = 15
livroC = 16
freqs = [livroA,livroB,livroC]


print(f'H1 (hipótese nula rejeitada), pois o Q² ({chisquare(freqs)[1]:.2%}) é menor do que a significância definida de {alpha:.2%}' if chisquare(freqs)[1] < alpha else f'H0 (hipótese nula aceita), pois o Q² ({chisquare(freqs)[1]:.2%}) é maior do que a significância definida de {alpha:.2%}')

print('Ou seja, as frequências observadas são muito diferentes da frequência esperada (20), então há preferências entre os livros.')