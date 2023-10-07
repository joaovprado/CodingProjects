import pandas as pd

# Criando o dataframe com duas colunas
df = pd.DataFrame({'coluna1': [1, 2, 2], 'coluna2': ['a', 'b', 'c']})

# Imprimindo o dataframe
print(df.describe())
