
#pip install pandas

from itertools import count
import pandas as pd

df = pd.read_csv('buscas.csv')  #abrindo csv
#print(df['comprou'])

X_df = df[['home', 'busca', 'logado']]
Y_df = df['comprou']

Xdummies_df = pd.get_dummies(X_df).astype(int)
Ydummies_df = Y_df

X = Xdummies_df.values    #devolvendo meu Df como um array
Y = Ydummies_df.values

# a eficacia do algoritmo quee chuta tudo um unico
acerto_de_um = len(Y[Y==1])
acerto_de_zero = len(Y[Y==0])
taxa_de_acerto_base = 100.0 * max(acerto_de_um, acerto_de_zero) / len(Y)


porcentagem_de_treino = 0.9

tamanho_de_treino = int(porcentagem_de_treino * len(Y))
tamanho_de_teste = len(Y) - tamanho_de_treino

treino_dados = X[:tamanho_de_treino]
treino_marcacoes = Y[:tamanho_de_treino]

teste_dados = X[-tamanho_de_teste:]
teste_marcacoes = Y[-tamanho_de_teste:]





from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit (treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)
diferencas = resultado - teste_marcacoes

acertos = [d for d in diferencas if d==0]
total_de_acertos = len(acertos)
total_de_elementos =  len(teste_dados)
taxa_acerto = 100.0 * total_de_acertos / total_de_elementos

print(f"Taxa de acerto base: {taxa_de_acerto_base}" )
print(f"Taxa de acerto do algoritmo: {total_de_acertos}")

