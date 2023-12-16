from scipy.special import comb
from scipy.stats import binom

probabilidade = lambda vitorias, jogadas, chance_vitoria: comb(jogadas-1, vitorias-1) * chance_vitoria**vitorias * (1-chance_vitoria)** (jogadas-vitorias)


# 3 acertos a cada 5 testes
# probabilidade de ter q fazer 20 testes para 12 acertos

prob = 3/5
jogadas = 20
vitorias = 12

print(f'A probabilidade é de {probabilidade(vitorias, jogadas, prob):.2%}')