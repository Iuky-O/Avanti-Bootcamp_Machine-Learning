
'''

    Para ler um arquivo CSV a biblioteca Pandas oferece a função:
        read_csv()
        
    E para exibir um numero N de linhas a biblioteca Pandas oferece a função:
        head() - junto com o numero expecífico de linhas
        
'''

import pandas as pd

df = pd.read_csv("data/meuarquivo.csv")

print(df.head(numero_linhas))
