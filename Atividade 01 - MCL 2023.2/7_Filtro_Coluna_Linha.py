'''

    Para selecionar uma coluna do DataFrame basta por:
    
        variavel["nome_coluna"]
        
    Para selecionar uma linha com uma condição basta por:
    
        variavel["nome_coluna"] condição
        
'''

import pandas as pd

df = pd.read_csv = ("data/meuarquivo.csv")

df["nome_coluna"]

df["nome_coluna"] > 10
