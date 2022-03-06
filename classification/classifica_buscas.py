
#pip install pandas

import pandas as pd

df = pd.read_csv('buscas.csv')  #abrindo csv
#print(df['comprou'])

X_df = df[['home', 'busca', 'logado']]
Y_df = df['comprou']

Xdummies_df = pd.get_dummies(X)
#Ydummies = pd.get_dummies(Y[1])
Ydummies_df = Y_df

X = Xdummies_df.values    #devolvendo meu Df como um array
Y = Ydummies_df.values


print()


