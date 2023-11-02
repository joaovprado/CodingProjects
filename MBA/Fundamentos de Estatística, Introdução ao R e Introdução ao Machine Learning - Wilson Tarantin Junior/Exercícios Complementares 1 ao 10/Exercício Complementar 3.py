from scipy.special import comb
from scipy.stats import binom

probabilidade = lambda vitorias, jogadas, chance_vitoria: comb(jogadas, vitorias) * chance_vitoria**vitorias * (1-chance_vitoria)** (jogadas-vitorias)

# chance de ter x vitorias em k rodadas = probabilidade(vitorias, rodadas, prob_vitoria)
# chance de ter x vitorias em k rodadas = binom.pmf(vitorias, rodadas, prob_vitoria)


prob_vitoria = 1/6 # Chance de 1/6 de vitória a cada rodada
rodadas = 10 # 10 rodadas

# Exercício 1 - Ter vitória em 4 jogadas
print(f"A probabilidade é de {probabilidade(4, rodadas, prob_vitoria):%}" ) # Calcular a probabilidade para 4 vitórias em 10 rodadas

# Exercício 2 - Ter vitória em pelo menos 7 jogadas
peloMenos7 = sum([binom.pmf(i, rodadas, prob_vitoria) for i in range(7,11)]) # Somar as probabilidades de 7, 8, 9 e 10 vitórias
print(f"A probabilidade é de {peloMenos7:%}" )