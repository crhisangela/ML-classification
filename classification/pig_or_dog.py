#py -m ensurepip --upgrade
#pip install -U scikit-learn
#pip3 install numpy scipy

from sklearn.naive_bayes import MultinomialNB

#INTRODUÇÃO: Entendendo a classificação utilizando as características de porcos e cachorros

#é gordinho / tem perninha curta / faz auau.
pig1 = [1, 1, 0]
pig2 = [1, 1, 0]
pig3 = [1, 1, 0]

dog1 = [1, 1, 1]
dog2 = [0, 1, 1]
dog3 = [0, 1, 1]

data = [pig1, pig2, pig3, dog1, dog2, dog3] #dados

reading = [1, 1, 1, -1, -1, -1] #marcações

idk1 = [1, 1, 1] #i dont know (eu nao sei)
idk2 = [1, 0, 0]

teste = [idk1, idk2]

model = MultinomialNB()
model.fit(data, reading) #treino
print(model.predict(teste)) #resultado / previsao
