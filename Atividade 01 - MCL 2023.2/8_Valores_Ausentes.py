'''

    Valores ausentes podem prejudicar a análise de dados, por isso é importante trata-los.
    A biblioteca Pandas oferece vários métodos para lidar com valores ausentes, entre eles:
        isna(), dropna() e fillna()
        
        isna() - verifica quais os valores ausentes, e retorna True(para valores NaN)/False(não NaN);
        
        fillna() - permite preencher os valores ausentes, com valores escolhidos. 
        
        dropna() - permite remover linhas com valores ausentes.
        
        
'''

import pandas as pd

df = pd.read_csv = ("data/meuarquivo.csv")


valores_ausentes = df.isna()                        #Exemplo isna()

df["nome_coluna".fillna(valor, inplace = True)      #Exemplo fillna()

df.dropna(inplace = True)                           #Exemplo drop()

