from scipy.stats import poisson  

k = 28/7
mu = 3

print(f'{poisson.pmf(k, mu):.2%}')