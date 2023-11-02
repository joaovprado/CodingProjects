from scipy.stats import norm

media = 26.5
desv = 4

def dist_normal(x, media, desv_padrao):
    return norm.cdf((x-media)/desv_padrao)

# P(X > 37)
X = 37
print(1-dist_normal(X, media, desv))


# P(X < 20)
X = 20
print(dist_normal(X, media, desv))


# P(22 < X < 28)
X1 = 22
X2 = 28
print(dist_normal(X2, media, desv) - dist_normal(X1, media, desv))